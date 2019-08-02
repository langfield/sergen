from terminalplot import plot
import pandas as pd
import numpy as np
import os

assert os.path.isdir("series/")
print("The following files are available to print (by entering `series/<name>.csv`):")
os.system("ls series/")
path = input("Enter the path to a saved curve as a csv: ")
raw_series = pd.read_csv(path)
series = np.array(raw_series)
y = list(series[:,1]) # Assumes 2-dimensional data. 
x = [i for i in range(series.shape[0])]
plot(x, y) 
print(series.shape)
