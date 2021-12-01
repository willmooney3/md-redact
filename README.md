# Markdown Redact
An extremely simple markdown extension that will optionally redact content from
a document.

# Installation
This extension is designed for [python-markdown](https://python-markdown.github.io/).

`pip install markdown md-redact`

# Usage
In your environment:

```shell
export MD_REDACT_CONTENT=1
```

In your markdown document:

```markdown
This is $some sensitive content$ in a markdown document.
```

In your Python code:

```python
import markdown


with open("filename.md", "r") as input_file:
    text = input_file.read()

html = markdown.markdown(, extensions=["md_redact"])

# html == '<p>This is <span class="redacted">(redacted)</span> in a markdown document.</p>'
```

Or from the command line:

```shell
MD_REDACT_CONTENT=1 python -m markdown -x md_redact filename.md
```

# Why?
Processing markdown for a project where some users were allowed to see specific
content while others were not. Figured an inline processor might be easier than
locking the users lacking permissions out of the page entirely.
