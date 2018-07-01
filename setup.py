#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 21:59:48 2018

@author: ivan
"""

from setuptools import setup, find_packages

setup(
    name='threshold-method-for-time-series',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='This package implements the threshold algorithm for decimation and collapsing of time series',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/ivangtorre/threshold-method-time-series',
    author='Ivan G Torre',
    author_email='ivan.gonzalez.torre@upm.es'
)