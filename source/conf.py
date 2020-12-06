import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}


project = 'python-plotting'
copyright = '2020, yues1130'
author = 'yues1130'

extensions = [
]



templates_path = ['_templates']

exclude_patterns = []


html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']