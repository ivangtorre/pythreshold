#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 21:55:01 2018

@author: ivan
"""

import numpy

def fahrToKelv(temp):
    '''
    takes a temperature `temp` in fahrenheit and returns it in Kelvin
    '''

    kelvin = 5./9. * (temp - 32.) + 273.15
    return kelvin

