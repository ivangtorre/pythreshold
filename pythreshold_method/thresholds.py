#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 21:33:40 2018

@author: ivan
"""
import os
import numpy as np
import scipy
import matplotlib.pyplot as plt


class time_series():
    """
    Create a time series object.
    """

    def __init__(self, file_path):
        """
        data is required to be a numpy series or a list
        :param file_path:
        """
        self.basename, self.file_extension = os.path.splitext(os.path.basename(file_path))
        self.file_path = file_path

    def import_data(self, square=True):

        if self.file_extension == ".wav":
            _, data_set = scipy.io.wavfile.read(self.file_path)

        elif self.file_extension == ".txt":
            data_set = np.loadtxt(self.file_path)

        if square == "True":
            data_set2 = np.power(data_set.astype(float), 2)

        elif square == "False":
            data_set2 = data_set

        self.plot_data(data_set)
        self.plot_data(data_set2)

    def plot_data(self, data):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(data)
        fig.savefig(self.basename + ".pdf")
