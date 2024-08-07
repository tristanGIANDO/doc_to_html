<h3 align="center">
    From docstrings to HTML file
</h3>

### A brief introduction

I developed this module to automate the creation of documentation.
It's just a bit of research to manipulate HTML. There's no deployment, it's all local.

The module uses all Python docstrings of the "Google" type to generate an HTML file.

# Prerequisites

Docstrings must be formatted as follows:

```py
"""
    Description

    Args:
        key: value

    Returns:
        description
"""
```

# INSTALL

First, check that you have Python 3 installed.

Run `pip3 install requirements.txt`.

Then, add the package folder to your `path` environment variable.

# USAGE

```py
from doc_to_html import main

main.generate_documentation(
        input_file="path/to/file.py"),
        output_directory="output/path")
    )

```
