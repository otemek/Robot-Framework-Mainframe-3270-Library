# -*- coding: utf-8 -*-
from .ExtendedMainframe3270.version import VERSION
from setuptools import setup


setup(name         		= 'robotframework-mainframe3270-extended',
      version      		= VERSION,
      description  		= 'Extended Mainframe Test library for Robot Framework based on Altran\'s library',
	  long_description	= 'Test library for Robot Framework to enable to create automated test scripts to test IBM Mainframe 3270',
      author       		= 'tom bsc',
      author_email 		= 'tom.bsc@outlook.com',
	  license      		= 'MIT License',
      url          		= 'https://github.com/otemek/robotframework-mainframe3270',
      packages  		= ['ExtendedMainframe3270'],
      package_data 		= {'ExtendedMainframe3270': []},
      requires     		= ['robotframework', 'six'],
      python_requires   = '>=3'
      )
