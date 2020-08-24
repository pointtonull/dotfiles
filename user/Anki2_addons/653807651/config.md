This add-on makes the following changes by default. If you don’t want one of them, simply change *true* to *false* below. You must restart Anki for the changes to take effect.

* **answerKeyCascade**: From the Answer Key Cascade add-on: pressing a value higher than the highest available ease automatically selects the highest available ease rather than doing nothing. *You may also wish to set cascadeButtonMappings; see below*.
* **easeShift**: All ease shortcuts are shifted down by one: Again becomes 0, Hard becomes 1, Good becomes 2, and Easy becomes 3. This allows you to keep your fingers on the bottom row with occasional reaches down for the fail key.
* **replayAudio**: Pressing `5` will trigger the Replay Audio action.
* **showAnswerUsingNumericalKeys**: From the Show Answer Using Numerical Keys add-on: pressing any ease button on the question side (including 0) will show the answer.
* **undoWithPeriod**: Pressing `.` undoes the previous review.

**cascadeButtonMappings** (*advanced*): If *answerKeyCascade* is not enabled, this will have no effect. If it is enabled, this allows you to choose an alternative method for mapping keypresses. The numbers in quotes represent the number of answer buttons that are available; so if there are 3 buttons shown, the options under "3" will be used. The numbers inside the square brackets represent what answer button will actually be triggered if the ease in its position is pressed. So if you set "2" to [null, 1, 1, 2, 2], if you press 1 or 2 Again (button 1) will be triggered and if you press 3 or 4 Good (button 2) will be triggered.

If you have *easeShift* on, then the four numbers you specify are used when you press 0, 1, 2, and 3/4 rather than 1, 2, 3, and 4, respectively, but the principle is the same.
