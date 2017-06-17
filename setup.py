#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages

setup(
    name = 'repomgr',
    packages = find_packages(),
    version = '0.2',
    description = 'Command-line tool for handling ROM repositor',
    author='José Luis Luri',
    author_email='jose.luis.luri@gmail.com',
    url='https://github.com/joseluisluri/repomgr',
    classifiers = [],
    install_requries=['pyyaml', 'tabulate']
)
