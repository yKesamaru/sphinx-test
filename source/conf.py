
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
    # 'sphinx_wagtail_theme'
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
    'show-inheritance': True
}

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
html_logo = 'https://raw.githubusercontent.com/yKesamaru/sphinx_documentation/master/assets/logo.png'
html_favicon = 'https://raw.githubusercontent.com/yKesamaru/sphinx_documentation/master/assets/logo.ico'
# html_theme = 'sphinx_wagtail_theme'
# html_theme_options = dict(
#     project_name="SPHINX-TEST",
#     logo="logo.png",
#     logo_alt="logo",
#     logo_height=50,
#     logo_width=50,
#     github_url="https://github.com/yKesamaru/sphinx_documentation/tree/master",
#     footer_links=",".join([
#         "About Us|https://pypi.org/project/sphinx-wagtail-theme/",
#         "wagtail github|https://github.com/wagtail/sphinx-wagtail-theme",
#         "wagtail document|https://sphinx-wagtail-theme.readthedocs.io/en/latest/",
#     ]),
# )
