# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

here=os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here,'README.rst')) as f:
    readme = f.read()

with open(os.path.join(here,'CHANGES.rst')) as f:
    changes = f.read()

with open(os.path.join(here,'LICENSE')) as f:
    license = f.read()

with open(os.path.join(here,'requirements.txt')) as f:
    requires = f.readlines()


requires.extend([

])
setup(
    name='__sample_project__',
    version='0.1.0.dev0',
    description='Sample package for __sample_project__',
    long_description=readme+'\n\n'+changes,
    author='XXXXXXXXX',
    author_email='XXXXXXXXXXX',
    url='XXXXXXXXXX',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    zip_safe=False,
    install_requires=requires,
)

