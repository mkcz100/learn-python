#!/usr/bin/env python

from distutils.core import setup

setup(name='Learn python',
      version='1.0',
      description='Project for python learning.',
      author='Michał Kuchmacz',
      python_requires='>=3.6, <4',
      install_requires=[
        'Pytest',
        'pymongo'
        ],
     )