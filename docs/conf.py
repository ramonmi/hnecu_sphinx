from datetime import date

project = "hnecu_sphinx"
copyright = "2021-%d, HNECU" % date.today().year
author = "Mi Ramon"

extensions = [
    "hnecu_sphinx",
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "numpydoc",
]
html_theme = "sphinx_rtd_theme"


def run_apidoc(_):
    import os
    import sys

    from sphinx.ext.apidoc import main

    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    module = os.path.join(cur_dir, "..", "hnecu_sphinx")
    main(
        [
            "-M",
            "--tocfile",
            "api_py",
            "-H",
            "API",
            "-o",
            os.path.join(cur_dir, "api_py"),
            module,
            "--force",
        ]
    )


def setup(app):
    app.connect("builder-inited", run_apidoc)


intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
