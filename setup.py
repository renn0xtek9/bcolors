#!/usr/bin/python3

#from distutils.core import setup
from setuptools import setup

long_description = """\
bcolors.py is a Python package that provide colors number to colorize output when you output to terminal
"""

setup(name='bcolors',
      version='0.1',
      description='Colorize output to terminal with python',
      long_description=long_description,
      author='Maxime Haseblauer',
      author_email='maxime.haselbauer@googlemail.com',	
      url='',
      #package_dir={'bcolors' : '.'},
      packages=['bcolors'],
     )