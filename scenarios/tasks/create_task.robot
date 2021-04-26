Documentation 	Task creation test for TodoMVC
*** Settings ***
Library						TodoMVC

*** Variables ***
@{EXISTING_TASKS}						task1		task2

*** Test Cases ***
Users can create task1
	[Tags]										good	essential
	When create new task			task1
	Then task should exist		task1

Users can create task2
	[Tags]										good	essential
	When create new task			task2
	Then task should exist		task2

Users can create " task3", the whitespace will be trimed
	[Tags]										good
	When create new task			${SPACE}task3
	Then task should exist		task3

Users cannot create empty Task
	[Tags]										bad	essential
	Given todo is empty
	And there are task				${EXISTING_TASKS}
	When create new task			${EMPTY}
	Then amount of task is		2

Users cannot create new task with only space character
	[Tags]										bad	essential
	Given todo is empty
	And there are task				${EXISTING_TASKS}
	When create new task			${SPACE}
	Then amount of task is		2

