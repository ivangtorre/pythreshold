#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 21:59:48 2018

@author: ivan
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pythreshold',
    version='0.1',
    packages=setuptools.find_packages(exclude=['tests*']),
    license='MIT',
    description='Threshold Method for time series implements the threshold algorithm for decimation and collapsing of time series',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/ivangtorre/threshold-method-time-series',
    author='ivangtorre',
    author_email='ivangonzaleztorre@gmail.com',
    
    test_suite='nose.collector',
    tests_require=['nose'],
    
    # name, etc...
    include_package_data=True,
)