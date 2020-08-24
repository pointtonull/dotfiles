"""
Numeric Keypad Remapping
Copyright 2014, 2016, 2018 Soren Bjornstad <anki@sorenbjornstad.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from aqt.reviewer import Reviewer
from aqt import mw
from aqt.utils import showCritical

ANSWER_KEYS = ('0', '1', '2', '3', '4')

conf = mw.addonManager.getConfig(__name__)
EASE_SHIFT                       = conf['easeShift']
UNDO_WITH_PERIOD                 = conf['undoWithPeriod']
ANSWER_KEY_CASCADE               = conf['answerKeyCascade']
SHOW_ANSWER_USING_NUMERICAL_KEYS = conf['showAnswerUsingNumericalKeys']
REPLAY_AUDIO                     = conf['replayAudio']


def cascadeConfigurationError(count, ease):
    showCritical("The 'cascadeButtonMappings' setting of the Numeric "
                 "Keypad Remapping add-on has been configured "
                 "incorrectly. Some information is missing about what "
                 "to do when there are %i buttons and answer button %i "
                 "is pressed. Please check your configuration and, if "
                 "necessary, reset it to the defaults."
                 % (count, ease))

# Function based on Kenishi's "Answer Key Cascade"
# and fisheggs' "Answer Key Remap"
_oldAnswerCard = Reviewer._answerCard
def newAnswerCard(self, ease):
    if ANSWER_KEY_CASCADE:
        # this could arise if EASE_SHIFT is on and 4 is pressed
        if ease > 4:
            ease = 4

        count = mw.col.sched.answerButtons(mw.reviewer.card) #Get button count
        try:
            ease = conf['cascadeButtonMappings'][str(count)][ease]
        except (KeyError, IndexError):
            cascadeConfigurationError(count, ease)
    _oldAnswerCard(self, ease)
Reviewer._answerCard = newAnswerCard


_oldDefaultEase = Reviewer._defaultEase
def newDefaultEase(self):
    defaultEase = _oldDefaultEase(self)
    count = self.mw.col.sched.answerButtons(self.card)

    # Depending on how we've configured the cascadeButtonMappings, it's
    # possible that the default ease could get mapped to Again/1, which is
    # probably not what we wanted. Therefore, if the default ease we currently
    # have *would* map to Again once the cascade is applied, try incrementing
    # the default ease choice until the target of the mapping is greater than
    # 1 or we run out of ease choices (this could happen if for some bizarre
    # reason we configured the mappings to map *every* button to 1).
    try:
        mappings = conf['cascadeButtonMappings'][str(count)]
        for mappingIndex in range(defaultEase, 5):
            if mappings[mappingIndex] > 1:
                defaultEase = mappingIndex
                break
    except (KeyError, IndexError):
        cascadeConfigurationError(count, defaultEase)

    return defaultEase
Reviewer._defaultEase = newDefaultEase


# Function partially based on Trey Bolyard's "Show answer using numerical keys"
oldShortcutKeys = Reviewer._shortcutKeys
def newShortcutKeys(self):
    def onAnswerButton(number):
        if EASE_SHIFT:
            number = number + 1
        if SHOW_ANSWER_USING_NUMERICAL_KEYS and self.mw.reviewer.state == "question":
            if number in (1, 2, 3, 4):
                self.mw.reviewer._showAnswer()
                return
        self._answerCard(number)

    def onUndoKey():
        try:
            if self.mw.col._undo[0] == 1:
                self.mw.onUndo()
        except TypeError:
            # no review to undo
            pass

    keymappings = oldShortcutKeys(self)
    # add additional functionality
    if EASE_SHIFT:
        keymappings.append(("0", lambda: onAnswerButton(0)))
    if REPLAY_AUDIO:
        keymappings.append(("5", lambda: self.mw.reviewer.replayAudio()))
    if UNDO_WITH_PERIOD:
        keymappings.append(("u", onUndoKey))

    # wrap existing answer button presses in our onAnswerButton function for
    # further functionality
    for index, (key, _) in enumerate(keymappings[:]):
        if key in ("1", "2", "3", "4"):
            def answerCaller(closureKey=key):
                return onAnswerButton(int(closureKey))
            keymappings[index] = (key, answerCaller)

    return keymappings
Reviewer._shortcutKeys = newShortcutKeys
