# deepmodeling_sphinx

[![pip install](https://img.shields.io/pypi/dm/hnecu_sphinx?label=pip%20install&logo=pypi)](https://pypi.org/project/hnecu_sphinx)
[![Documentation Status](https://readthedocs.org/projects/hnecu-sphinx/badge/)](https://hnecu-sphinx.readthedocs.io/)

This package should be used in the sphinx projects authored by HNECU Group.

## Features

- Add the custom banner
- Minify HTML, Javascript, and CSS files
- Supports dark mode for both the banner and the RTD theme

## How to use it

### Setup

Add `hnecu_sphinx` to the requirements, as well as the `extensions` of `conf.py`:

```py
extensions = [
    'hnecu_sphinx',
]
```

Projects outside HNECU can also use this extension but disable HNECU specific styles.

```py
# default: True
enable_hnecu = False
```

### Render list of authors

The following directive can be used to render list of authors from `git shortlog`:

```rst
.. git-shortlog-authors::

```
