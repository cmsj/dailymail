#!/usr/bin/python
"""
dump_readme

Extract the docstring from our main source and write it to README.md
"""

import __init__

DOCS = __init__.__doc__
README = open("README.md", "w")
README.write(DOCS)
README.close()
