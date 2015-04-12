'''
Gauged - https://github.com/chriso/gauged
Copyright 2014 (c) Chris O'Hara <cohara87@gmail.com>
'''

import sys
import re
import os.path

PY3 = sys.version_info[:2] >= (3, 0)

try:
    from ez_setup import use_setuptools

    use_setuptools()
except ImportError:
    pass  # Nothing to do about it

from setuptools import setup, Extension, find_packages

dir =  os.path.dirname(__file__)

cflags = ['-O3', '-std=c99', '-pedantic', '-Wall', '-Wextra', '-pthread', '-I%s' % os.path.join(dir, 'include')]


gauged = Extension(
    '_gauged',
    sources=[os.path.join(dir, 'lib', '%s.c' % src) for src in ('array', 'hash', 'sort', 'map', 'writer')],
    include_dirs=['include'],
    extra_compile_args=cflags
)

version_file = os.path.join(
    dir,
    'gauged',
    'version.py'
)

with open(version_file, 'r') as handle:
    version = re.search(r'__version__ = \'([^\']+)\'', handle.read(), re.M).group(1)

if PY3:
    test_suite = 'tests.py3.run_tests'
else:
    test_suite = 'tests.py2.run_tests'

setup(
    name='gauged',
    version=version,
    author='Chris O\'Hara',
    author_email='cohara87@gmail.com',
    description='A fast, append-only storage layer for numeric data that changes over time',
    license='MIT',
    url='https://github.com/chriso/gauged',
    ext_modules=[
        gauged
    ],
    install_requires=[
        'six'
    ],
    packages=find_packages(exclude=('test',)),
    test_suite=test_suite
)
