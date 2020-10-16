# -*- coding: utf-8 -*-
from os.path import abspath, dirname, join

try:
    from setuptools import setup
except ImportError as error:
    from distutils.core import setup


version_file = join(dirname(abspath(__file__)), 'Mainframe3270', 'version.py')

with open(version_file) as file:
    code = compile(file.read(), version_file, 'exec')
    exec(code)

setup(name         		= 'robotframework-mainframe3270',
      version      		= '1.2.1.dev0',
      description  		= 'Mainframe Test library for Robot Framework',
	  long_description	= 'Test library for Robot Framework to enable to create automated test scripts to test IBM Mainframe 3270',
      author       		= 'tom bsc',
      author_email 		= 'tom.bsc@outlook.com',
	  license      		= 'MIT License',
      url          		= 'https://github.com/otemek/robotframework-mainframe3270',
      packages  		= ['robotframework-mainframe3270'],
      package_data 		= {'robotframework-mainframe3270': []},
      requires     		= ['robotframework', 'six'],
      python_requires   = '>=3'
      )
