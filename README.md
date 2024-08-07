<h3 align="center">
    From docstrings to HTML file
</h3>

### A brief introduction
I developed this module to automate the creation of documentation.

The module uses all Python docstrings of the "Google" type to generate an .html file.

# INSTALL
First, check that you have Python 3 installed.

`ast` and `jinja2` are required. Install them with `pip install`.

Then, add the package folder to your `path` environment variable.

### USAGE
```py
from doc_to_html import main

main.generate_documentation(
        input_file="path/to/file.py"),
        output_directory="output/path")
    )

```
