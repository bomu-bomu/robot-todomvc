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

## Development

### Convention and .editorconfig

In both robot and python file, we apply the same basis:

- 4-width spaces instead of tabs
- No trailing whitespace
- New line at the end of file

You can use editorconfig plugin on any editor to make the same convention
across developers.

#### vim

If you use vim8 you can use as plugin

```
mkdir -p ~/.vim/pack/local/start
cd ~/.vim/pack/local/start
git clone https://github.com/editorconfig/editorconfig-vim.git
```

#### VS Code

[Install EditorConfig for VS Code](vscode:extension/EditorConfig.EditorConfig)
