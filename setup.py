#!/usr/bin/env python

from setuptools import setup, find_namespace_packages

print(find_namespace_packages())

setup(name='Learn python',
      version='1.0',
      description='Project for python learning.',
      author='Michał Kuchmacz',
      python_requires='>=3.6, <4',
      packages=find_namespace_packages(),
      install_requires=[
          'pytest',
          'pymongo',
          'dotenv',
          'numpy'
      ],
      )
