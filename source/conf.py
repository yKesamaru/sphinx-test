
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sys
import os

sys.path.append(os.path.abspath(".."))
for i in sys.path:
    print(i)
# exit(0)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SPHINX-TEST'
copyright = '2024, USER'
author = 'USER'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
]
# Napoleon settings
napoleon_google_docstring = True
# Autodoc settings
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'special-members': True,
    'inherited-members': True,
    'show-inheritance': True,
}

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
html_logo = 'https://raw.githubusercontent.com/yKesamaru/FACE01_DEV/master/assets/images/Logo_dist.png'
html_favicon = 'https://raw.githubusercontent.com/yKesamaru/FACE01_DEV/master/assets/images/Logo.ico'
