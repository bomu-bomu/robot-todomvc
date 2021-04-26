
*** Keywords ***
There are existing tasks ${tasks}
	Given todo is empty
	And there are task		${tasks}

check done for task "${task}"
	done task				${task}

"${task}" should be strikethroughed
	Is task completed 		${task}

the item count decrease to ${amount}
	${count} =				get item amount
	Should Be Equal			${count}	${amount}
