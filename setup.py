#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from tidehunter import __version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'tidehunter'
]

with open('requirements.txt') as f:
    requires = f.read().strip().splitlines()

with open('LICENSE') as f:
    license = f.read().strip()

with open('README.rst') as f:
    readme = f.read().strip()

with open('CHANGES.rst') as f:
    changes = f.read().strip()

long_description = readme + '\n\n' + changes

setup(
    name='tidehunter',
    version=__version__,
    description='HTTP streaming with accurate flow control',
    long_description=long_description,
    author='Runzhou Li (Leo)',
    author_email='runzhou.li@gmail.com',
    url='https://github.com/woozyking/tidehunter',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'tidehunter': 'tidehunter'},
    include_package_data=True,
    install_requires=requires,
    license=license,
    zip_safe=False,
    classifiers=(
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'
    ),
)
