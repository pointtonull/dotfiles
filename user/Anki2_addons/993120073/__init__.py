from anki import stats
from anki.lang import _
from anki.hooks import wrap
from aqt import mw


def get_tooltip_html():
	return (
		f"""\
<table id="correct-answers-tooltip">
	<tr>
		<td style="color: {stats.colLearn};">{_("Learn")}</td>
		<td></td>
		<td></td>
		<td> / </td>
		<td></td>
	</tr>
	<tr>
		<td style="color: {stats.colRelearn};">{_("Relearn")}</td>
		<td></td>
		<td></td>
		<td> / </td>
		<td></td>
	</tr>
	<tr>
		<td style="color: {stats.colYoung};">{_("Young")}</td>
		<td></td>
		<td></td>
		<td> / </td>
		<td></td>
	</tr>
	<tr>
		<td style="color: {stats.colMature};">{_("Mature")}</td>
		<td></td>
		<td></td>
		<td> / </td>
		<td></td>
	</tr>
</table>"""
		"""\
<style>
#correct-answers-tooltip {
	position: absolute;
	display: none;
	padding: 2px;
	border: 1px solid #ddd;
	background: #fff;
	color: #000;
	opacity: 0.9;
}
body.night_mode #correct-answers-tooltip {
	border-color: #222;
	background: #2f2f31;
	color: #fff;
}
#correct-answers-tooltip td:nth-child(1) {
	font-weight: bold;
}
#correct-answers-tooltip td:nth-child(2) {
	font-weight: bold;
	text-align: right;
	min-width: 5em;
}
#correct-answers-tooltip td:nth-child(3) {
	text-align: right;
	min-width: 3em;
}
#correct-answers-tooltip td:nth-child(5) {
	text-align: right;
}
</style>
<script>
$(function () {
	let tooltip = $("#correct-answers-tooltip").appendTo("body");
	let placeholder = $("#correct-answers");
	placeholder.bind("plothover", function (event, pos, item) {
		if (!item) {
			tooltip.finish().hide();
			return;
		}
		let plot = placeholder.data("plot");
		let day = item.datapoint[0];
		let data = plot.getData();
		tooltip.css({
			top: item.pageY + 10,
			left: item.pageX + 10
		}).delay(100).fadeIn(200);
		tooltip.find("tr").each(function (index) {
			let tr = $(this);
			let total = data[3 - index].data.find(e => e[0] === day);
			if (total && total[1] > 0) {
				total = total[1];
				let percentage = data[index + 4].data.find(e => e && e[0] === day)[1];
				tr.children(":nth-child(2)").text(percentage.toFixed(1) + "%");
				tr.children(":nth-child(3)").text((percentage / 100 * total).toFixed(0));
				tr.children(":nth-child(5)").text(total);
				tr.show();
			}
			else {
				tr.hide();
			}
		});

	}).bind("plothovercleanup", function () {
		tooltip.finish().hide();
	});
});
</script>"""
	)


def get_data(self, combine_relearn):
	cutoff = self.col.sched.dayCutoff
	end, chunk = self.get_start_end_chunk()[1:]
	conds = []

	revlog_limit = self._revlogLimit()
	if revlog_limit:
		conds.append(revlog_limit)

	days = self._periodDays()
	if days:
		conds.append(f"id > {(cutoff - days * 86400) * 1000}")

	where_expression = f"WHERE {' AND '.join(conds)}" if conds else ""
	data = self.col.db.all(
		f"""\
WITH answers AS (
	SELECT
		ease,
		(id / 1000 - ?1) / 86400 / ?2 AS day,
		(CASE
			WHEN type = 0 THEN 0
			WHEN type = 2 THEN ?3
			WHEN lastIvl < 21 THEN 2
			ELSE 3
		END) AS thetype
	FROM revlog {where_expression}
)
SELECT
	day,
	thetype,
	SUM(ease > 1),
	COUNT(*)
FROM answers
GROUP BY day, thetype
ORDER BY day""",
		cutoff,
		chunk,
		(1 if not combine_relearn else 0)
	)

	return data, end, chunk


def get_graph_points(data):
	points = ([], [], [], [])
	day_type_totals = {}
	days = set()
	for day, thetype, correct, total in data:
		p = points[thetype]
		if p and p[-1][0] != day - 1:
			p.append(None)
		p.append((day, correct / total * 100.0))

		day_type_totals[(day, thetype)] = total
		days.add(day)

	totals = ([], [], [], [])
	for day in sorted(days):
		for thetype in range(4):
			totals[thetype].append((
				day,
				day_type_totals.get((day, thetype), 0)
			))

	return points, totals


def answer_graph(self):
	txt = self._title(_("Correct Answers"), _("The percentage of answers that were correct."))

	config = mw.addonManager.getConfig(__name__)
	combine_relearn = config.get("combine_learn_and_relearn")

	data, end, chunk = get_data(self, combine_relearn)
	points, totals = get_graph_points(data)

	xmin = -end + 0.5 if end else data[0][0] - 0.5 if data else None

	def cfg(graph):
		show = not config.get(f"hide_{graph}")
		return {
			"bars": {"show": False},
			"lines": {"show": show},
			"points": {"show": show}
		}

	txt += self._graph(
		id="correct-answers",
		data=(
			{"data": totals[3], "stack": 0, "yaxis": 2, "color": stats.colMature},
			{"data": totals[2], "stack": 0, "yaxis": 2, "color": stats.colYoung},
			{"data": totals[1], "stack": 0, "yaxis": 2, "color": stats.colRelearn},
			{"data": totals[0], "stack": 0, "yaxis": 2, "color": stats.colLearn},
			{"data": points[0], "stack": 1, **cfg("learn"),	"label": _("Learn"), "color": stats.colLearn},
			{"data": points[1], "stack": 2, **cfg("relearn"),
				"label": _("Relearn") if not combine_relearn else None, "color": stats.colRelearn},
			{"data": points[2], "stack": 3, **cfg("young"),	"label": _("Young"), "color": stats.colYoung},
			{"data": points[3], "stack": 4, **cfg("mature"), "label": _("Mature"), "color": stats.colMature}
		),
		conf={
			"xaxis": {"min": xmin, "max": 0.5},
			"yaxes": (
				{"min": 0, "max": 105},
				{"min": 0, "position": "right"}
			),
			"grid": {"hoverable": True}
		},
		xunit=chunk,
		ylabel=_("% Correct"),
		ylabel2=_("Answers")
	)

	txt += get_tooltip_html()
	return txt


def new_ease_info(self, eases, _old):
	txt = _old(self, eases)
	txt += answer_graph(self)
	return txt


stats.CollectionStats._easeInfo = wrap(stats.CollectionStats._easeInfo, new_ease_info, pos="around")
