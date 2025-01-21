# CopyCode

**CopyCode** is a CLI tool that gathers your source code files and copies them to your clipboard or saves them to a file. It is especially useful when you want to quickly provide your project's code to AI tools like ChatGPT. The package also displays the number of files processed, total lines of code, and a list of processed files.

## Features

- Copies `.py`, `.js`, and `.html` by default, or any extensions specified via configuration or command-line arguments.
- Excludes any files or directories you specify in the config file or with the `--exclude` flag.
- Generates a header before each file in the combined output.
- Outputs statistics including the number of files processed and total lines of code.
- Displays the names of all processed files.
- Optionally exports the combined code to a text file instead of just copying to the clipboard.
- Open source, MIT-licensed.
- can be configured using a config file

## Installation

```bash
pip install copycode
```
# Usage

```bash
copycode [path] [--exclude=files_or_folders] [--filetypes=.py,.js,...] [--outfile=output.txt]
```
## other examples
### Copy all .py, .js, and .html files from the current directory
```bash
copycode
```

### Specify a different path
```bash
copycode /path/to/project
```

### Exclude multiple files or folders
```bash
copycode . --exclude=secret.py,test.py
```

### Specify filetypes to process instead of the defaults
```bash
copycode . --filetypes=.py,.ts
```

### Save the output to a file instead of copying to clipboard
```bash
copycode . --outfile=all_code.txt
```

## Installation

You can create a file named .copyconfig in your project or working directory. By default, copycode looks for a file named .copyconfig in the same directory as the main.py script. If it is not found, the defaults are used.

Below is an example .copyconfig file:

```yaml
filetypes:
  - .py
  - .js
  - .html

exclude:
    - secret.py
    - node_modules
 ```

If you do not provide a config file, copycode defaults to excluding nothing and processing .py, .js, and .html files only.
Any command-line arguments (like --exclude or --filetypes) will override or replace values from the config file.