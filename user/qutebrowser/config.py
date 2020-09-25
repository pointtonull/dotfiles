config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36",
    "https://*.slack.com/*",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}",
    "https://web.whatsapp.com/",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0",
    "https://accounts.google.com/*",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0",
    "https://docs.google.com/*",
)
config.set("content.images", True, "chrome-devtools://*")
config.set("content.images", True, "devtools://*")
config.set("content.javascript.enabled", True, "chrome-devtools://*")
config.set("content.javascript.enabled", True, "chrome://*/*")
config.set("content.javascript.enabled", True, "devtools://*")
config.set("content.javascript.enabled", True, "qute://*/*")
config.set(
    "content.register_protocol_handler",
    True,
    "https://mail.google.com?extsrc=mailto&url=%25s",
)

# c.qt.args = ["blink-settings=darkMode=4"]
# config.set("colors.webpage.prefers_color_scheme_dark", True)

c.hints.scatter = True
# c.hints.selectors["all"].append("li")
c.hints.selectors["all"].append("li.ResultList-item > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)")
c.hints.selectors["all"].append('input[id="unread"]')
c.hints.selectors["all"].append("label")
c.hints.selectors["all"].append('p[class="ConvoRow-body"]')
c.hints.selectors["checkbox"] = []
c.hints.selectors["checkbox"].append('[role="checkbox"]')
c.hints.hide_unmatched_rapid_hints = True
c.tabs.background = True
c.tabs.close_mouse_button = "middle"
c.tabs.last_close = "blank"
c.tabs.new_position.related = "last"
c.tabs.new_position.stacking = False
c.tabs.new_position.unrelated = "last"
c.tabs.position = "top"
c.tabs.select_on_remove = "next"

config.bind(",b", "hint all tab-bg")
config.bind(",d", "tab-close ;; tab-focus 1")
config.bind(",l", "tab-move -1 ;; tab-next")
config.bind(",m", "hint --rapid all tab-bg")
config.bind(",c", "hint --rapid checkbox")
config.bind(",n", "scroll-page 0 0.9 ;; tab-move -1 ;; tab-focus 1")
config.bind(",r", "tab-close ;; undo ;; tab-move -1 ;; tab-focus 1")
config.bind(",t", "hint all tab-bg ;; hint all tab-bg")
config.bind(",u", "undo ;; tab-move -1 ;; tab-focus 1")
config.bind(",ve", "config-edit")
config.bind("h", "tab-prev")
config.bind("l", "tab-next")

