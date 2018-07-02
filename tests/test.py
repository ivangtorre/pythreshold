#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 21:57:09 2018

@author: ivan
"""

from pythreshold.thresholds import time_series
import unittest
import os


TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), '../data/', 'data1.txt')


class TestThreshold(unittest.TestCase):

    def test_initialite(self):
        th_data = time_series(TESTDATA_FILENAME)
        th_data.import_data()


if __name__ == '__main__':
    unittest.main()  # pragma: no cover