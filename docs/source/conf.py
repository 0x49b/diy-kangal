# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Kangal'
copyright = '2022, lichtwellenreiter'
author = 'Lichtwellenreiter'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'alabaster'
html_theme_options = {
    'logo': 'https://ih1.redbubble.net/image.424837183.4243/st,small,507x507-pad,600x600,f8f8f8.u5.jpg',
    'github_user': 'lichtwellenreiter',
    'github_repo': 'diy-kangal',
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
