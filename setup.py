from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import aipu

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.txt', 'CHANGES.txt')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='aipu',
    version=sandman.__version__,
    url='https://github.com/Tekvot/aipu.git',
    license='Apache Software License',
    author='Tekvot Community',
    tests_require=['pytest'],
    install_requires=[''],
    cmdclass={'test': PyTest},
    author_email='erick.sorogastua@gmail.com',
    description='Artificial Intelligence Processing Unit',
    long_description=long_description,
    packages=['aipu'],
    include_package_data=True,
    platforms='any',
    test_suite='aipu.test.test_aipu',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 0 - Beta',
        'Natural Language :: Spanish',
        'Environment :: Dev', 
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Alpine',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
