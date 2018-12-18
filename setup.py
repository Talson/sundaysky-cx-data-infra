# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sundaysky-cx-data-infra',
    version='0.1.0',
    description='CX Data Infra',
    long_description=readme,
    author='Data Team',
    author_email='tal.elson@sundaysky.com',
    url='https://github.com/SundaySky/sundaysky-cx-data-infra',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

