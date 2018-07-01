#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 21:57:09 2018

@author: ivan
"""

from pythreshold_method.thresholds import time_series

th_data = time_series("./../data/data1.txt")
th_data.import_data()
