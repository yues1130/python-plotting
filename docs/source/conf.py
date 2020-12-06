import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
project = 'python-plotting'
copyright = '2020, yues1130'
author = 'yues1130'
release = '1.0.0'
html_baseurl = 'https://yues1130.github.io/python-plotting/'
extensions = [
    'sphinx.ext.githubpages',
]
templates_path = ['_templates']
language = 'ko'
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']