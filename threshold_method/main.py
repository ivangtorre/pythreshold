#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 21:33:40 2018

@author: ivan
"""

class time_series():
    """
    Create a time series object.
    """
    def __init__(self):
        """
        data is required to be a numpy series or a list
        """

    def importdata(self, filepath, square=True):
        import os
        import scipy
        import numpy as np
        self.basename, self.file_extension = os.path.splitext(os.path.basename(filepath))
        
        if self.file_extension == ".wav":
            _, dataset = scipy.io.wavfile.read(self.filepath)

        elif self.file_extension == ".txt":
            self.dataset = np.loadtxt(self.filepath)
        
        if square == "True":
            self.dataset2 = np.power(self.dataset.astype(float), 2)
        
        elif square == "False":
            self.dataset2 = self.dataset
        
        
    def plot_dataset(self):
        import matplotlib.pyplot as plt
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax.plot(self.dataset)
        
        