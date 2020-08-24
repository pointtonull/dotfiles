# -*- coding: utf-8 -*-
"""
Anki Add-on: Hint Hotkeys

Adds two hotkeys to the reviewer: 'H' to reveal hints one by one,
'G' to reveal all hints at once.

Based on "Hint-peeking Keyboard Bindings" by Ben Lickly

Copyright:  (c) Ben Lickly 2012 <blickly at berkeley dot edu>
            (c) Glutanimate 2016-2017 <https://glutanimate.com/>
License: GNU AGPLv3 or later <https://www.gnu.org/licenses/agpl.html>
"""

from __future__ import unicode_literals

############## USER CONFIGURATION START ##############

# Shortcuts need to be single keys on Anki 2.0.x
# Key combinations are supported on Anki 2.1.x

# Shortcut that will reveal the hint fields one by one:
SHORTCUT_INCREMENTAL = "."
# Shortcut that will reveal all hint fields at once:
SHORTCUT_ALL = "7"

##############  USER CONFIGURATION END  ##############

from aqt.qt import *
from aqt import mw
from aqt.reviewer import Reviewer

from anki.hooks import wrap, addHook
from anki import version as ankiversion


def _newKeyHandler(self, evt, _old):
    """Add shortcuts on Anki 2.0.x"""
    if evt.key() == QKeySequence(SHORTCUT_INCREMENTAL)[0]:
        _showHint(incremental=True)
    elif evt.key() == QKeySequence(SHORTCUT_ALL)[0]:
        _showHint()
    return _old(self, evt)


def _addShortcuts(shortcuts):
    """Add shortcuts on Anki 2.1.x"""
    show_next = (SHORTCUT_INCREMENTAL,
                 lambda: _showHint(incremental=True))
    show_all = (SHORTCUT_ALL, _showHint)

    for pos, shortcut in enumerate(shortcuts):
        if shortcut[0] == SHORTCUT_INCREMENTAL:
            shortcuts[pos] = show_next
            show_next = None
        elif shortcut[0] == SHORTCUT_ALL:
            shortcuts[pos] = show_all
            show_all = None

    if show_next:
        shortcuts.append(show_next)
    if show_all:
        shortcuts.append(show_all)


def _showHint(incremental=False):
    """Show hint by activating corresponding links."""
    mw.web.eval("""
     var customEvent = document.createEvent('MouseEvents');
     customEvent.initEvent('click', false, true);
     var arr = document.getElementsByTagName('a');
     // Cloze Overlapper support
     if (typeof olToggle === "function") { 
         olToggle();
     }
     // Image Occlusion Enhanced support
     var ioBtn = document.getElementById("io-revl-btn");
     if (!(typeof ioBtn === 'undefined' || !ioBtn)) { 
         ioBtn.click();
     }
     for (var i=0; i<arr.length; i++) {
        var l=arr[i];
        if (l.style.display === 'none') {
          continue;
        }
        if (l.href.charAt(l.href.length-1) === '#') {
          l.dispatchEvent(customEvent);
          if ('%s' === 'True') {
            break;
          }
        }
     }
     """ % incremental)


# Hooks and Patches

if ankiversion.startswith("2.0"): # 2.0.x
    Reviewer._keyHandler = wrap(
        Reviewer._keyHandler, _newKeyHandler, "around")
else: # 2.1.x
    addHook("reviewStateShortcuts", _addShortcuts)
