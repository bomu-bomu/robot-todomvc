# Robotframework Demonstration for TodoMVC

## Installation

```
pip3 install robotframework
pip3 install robotframework-seleniumlibrary
```

## Pre Running

Preset Robotframework environment
This will set up ROBOT_OPTIONS before running

```
source .initial.sh
```

## Running

Run all scenarios

```
robot scenarios
```

Run only good tags

```
robot --include good scenarios
```

Run only tasks folder

```
robot scenarios/tasks
```
