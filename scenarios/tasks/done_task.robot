Documentation       Test suite for done task for TodoMVC
*** Settings ***
Library             TodoMVC
Resource            ${resources}/task_keywords.robot

*** Variables ***
@{EXISTING_TASKS}   task1   task2

*** Test Cases ***
Done task
    [Tags]          good    essential
    Given there are existing tasks ${EXISTING_TASKS}
    When check done for task "task1"
    Then "task1" should be strikethroughed
    And the item count decrease to 1
