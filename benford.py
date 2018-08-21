import sys
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
        try:
            while x_str[0] in prefixes:
                x_str = x_str[1:]

            first = int(x_str[0])
            return first
        except:
            # print("Problem with {}".format(x))
            return np.nan


    def convert_dataset(self):
        """Convert the dataset to its first digit equivalent."""
    
        self.data_first_digit = self.data.applymap(self.first_digit) 
        self.data_first_digit = self.data_first_digit.dropna()

    def plot_theory_hist(self, fig=None, label="theory"):

        x = range(1,10)
        benford_probability = [np.log10(1+1/xx) for xx in x ]
        plt.figure(fig)
        plt.plot(x, benford_probability, label=label)


    def plot_first_digit_hist(self, title=None, fig=None, label="data"):

        data = self.data_first_digit
        
        fig, ax = plt.subplots(num=fig)
        data.hist(bins=np.arange(0.5, 10, 1), ax=ax,
            density=True, stacked=True, align="mid", label=label) #, histtype="step"  )
        plt.xticks(range(1,10))
        plt.xlim([0,10])
        plt.xlabel("First Digit")
        plt.ylabel("Frequency")
        plt.title(title)


    def plot_raw_data_hist(self, data=None, title=None, fig=None):

        data = self.data
        
        data.hist(bins=30, density=True, stacked=True, align="mid") #, histtype="step"  )
        # plt.xticks(range(1,10))
        # plt.xlim([0,10])
        # plt.xlabel("First Digit")
        plt.xlabel("Data Values")
        plt.ylabel("Frequency")
        plt.title(title)



if __name__ == "__main__":
    
    fname = sys.argv[1]
    title = fname.rpartition("/")[2].partition(".")[0]

    ben = Benford(fname, fname)
    ben.convert_dataset()

    # Plot the first digit distribution
    fig = 10
    plt.figure(fig)
    ben.plot_first_digit_hist(fig=fig, title=title)
    ben.plot_theory_hist(fig=fig)
    plt.legend()
    plt.tight_layout()
    plt.savefig(title+".pdf")

    ben.plot_raw_data_hist(title=title)
    plt.tight_layout()
    plt.savefig(title+"_raw.pdf")
