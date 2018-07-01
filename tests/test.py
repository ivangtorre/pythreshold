#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 21:57:09 2018

@author: ivan
"""

from pythreshold_method.thresholds import time_series

def test_fahrToKelv():
    '''
    make sure freezing is calculated correctly
    '''
    
    assert somePython.fahrToKelv(32) == 273.15, 'incorrect freezing point!'
