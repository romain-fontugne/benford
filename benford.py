import numpy as np
import pandas as pd
from matplotlib import pylab as plt

class Benford(object):

    """Compute the distribution of first digit from a dataset."""

    def __init__(self, datafile="test.csv", dataname="Test"):
        """Intialisation of the Benford. 
        
        Parameters:
            datafile: Filename for the dataset (one column file)"""

        self.datafile = datafile
        self.dataname = dataname
        self.data = pd.read_csv(self.datafile,header=None)
        self.data_first_digit = None
        
    def first_digit(self,x):
        """Return the first digit of x."""

        prefixes = ["0", ".", "-"]
        x_str = str(float(x))
        while x_str[0] in prefixes:
            x_str = x_str[1:]

        first = int(x_str[0])
        return first


    def convert_dataset(self):
        """Convert the dataset to its first digit equivalent."""
    
        self.data_first_digit = self.data.applymap(self.first_digit) 

    def plot_distribution(self):
        
        plt.figure()
        self.data_first_digit.hist()
        plt.title(self.dataname)
        plt.show()
