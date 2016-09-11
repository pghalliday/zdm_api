#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.1.0'

if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='zdm_api',
    version=version,
    description="""Zipped dependency manager API""",
    long_description=readme + '\n\n' + history,
    author='Peter Halliday',
    author_email='pghalliday@gmail.com',
    url='https://github.com/pghalliday/zdm_api',
    packages=[
        'zdm_api',
    ],
    include_package_data=True,
    install_requires=[
        'django-model-utils>=2.0',
        'djangorestframework>=3.4,<3.5',
        'drf-extensions==0.3.1',
        'django-rest-swagger>=2.0,<2.1',
        'coreapi>=2.0,<2.1',
    ],
    dependency_links=[
        'git+https://github.com/chibisov/drf-extensions.git@master#egg=drf-extensions-0.3.1',
    ],
    license="MIT",
    zip_safe=False,
    keywords='zdm_api',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
