# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 19:14:57 2020

@author: jaredalbert
working with results

"""
#%%
import pandas as pd
import numpy as np
import scipy
from sklearn.preprocessing import StandardScaler
import scipy.stats
import matplotlib.pyplot as plt

path_spy='C:/Users/jaredalbert/Desktop/python_scripts/IPO_study/SPY.csv'
df = pd.read_csv(path_spy, parse_dates=True)
df['Date']=pd.to_datetime(df['Date'])
df = df.set_index(df['Date'])
df['ln_change'] = (np.log(df['Adj Close']/df['Adj Close'].shift(1)))
df.ln_change.dropna(inplace=True)

y=np.array(df.ln_change)

x = np.arange(len(y))
size = len(y)

ds_df = pd.DataFrame(y, columns = ['LN_change'])


sc=StandardScaler()
yy = y.reshape (-1,1)
sc.fit(yy)
y_std =sc.transform(yy)
y_std = y_std.flatten()

#%%
results=pd.read_csv('C:/Users/jaredalbert/AppData/Local/Programs/Python/Python36-32/learning_testing/Find_Distribution/results_fit_local.csv')
# Divide the observed data into 100 bins for plotting (this can be changed)
print(results.head())
#%%
#results = results.drop(0)
number_of_bins = 100
bin_cutoffs = np.linspace(np.percentile(y,0), np.percentile(y,99),number_of_bins)

# Create the plot
h = plt.hist(y, bins = bin_cutoffs, color='0.75')

# Get the top three distributions from the previous phase
number_distributions_to_plot = 10
dist_names = results['Distribution'].iloc[0:number_distributions_to_plot]
#dist_names ='norm'
# Create an empty list to store fitted distribution parameters
parameters = []

# Loop through the distributions ot get line fit and paraemters

for dist_name in dist_names:
    # Set up distribution and store distribution paraemters
    dist = getattr(scipy.stats, dist_name)
    #dist = getattr(scipy.stats, 'norm')
    param = dist.fit(y)
    parameters.append(param)

    # Get line for each distribution (and scale to match observed data)
    pdf_fitted = dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1])
    scale_pdf = np.trapz (h[0], h[1][:-1]) / np.trapz (pdf_fitted, x)
    pdf_fitted *= scale_pdf

    # Set the plot x axis to contain 99% of the data
    # This can be removed, but sometimes outlier data makes the plot less clear
    plt.xlim(np.percentile(y,0),np.percentile(y,99))

    # Add the line to the plot
    plt.plot(pdf_fitted, label=dist_name)



# Add legend and display plot

plt.legend()
plt.show()

# Store distribution paraemters in a dataframe (this could also be saved)
dist_parameters = pd.DataFrame()
dist_parameters['Distribution'] = (
        results['Distribution'].iloc[0:number_distributions_to_plot])
dist_parameters['Distribution parameters'] = parameters

# Print parameter results
print ('\nDistribution parameters:')
print ('------------------------')

for index, row in dist_parameters.iterrows():
    print ('\nDistribution:', row[0])
    print ('Parameters:', row[1] )

##%%
##plt.hist(y, bins = bin_cutoffs, color='0.75')
#plt.plot(bin_cutoffs,norm.pdf(bin_cutoffs,param[0], param[1]))
#plt.xlim(np.percentile(y,0),np.percentile(y,99))
#plt.show()
##%%
#%%
#import numpy as np
#from scipy.stats import johnsonsu
#import matplotlib.pyplot as plt
number_distributions_to_plot = 10
dist_names = results['Distribution'].iloc[0:number_distributions_to_plot]

# Generate some data for this demonstration.
data = y

# Fit a distribution to the data:
#param = johnsonsu.fit([data])

# Plot the histogram.
plt.hist(data, bins=300, density=True, alpha=0.6, color='g')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)

parameters = []
for dist_name in dist_names:
    # Set up distribution and store distribution paraemters
    dist = getattr(scipy.stats, dist_name)
    param = dist.fit(y)
    parameters.append(param)

    pdf_fitted= dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1])

    plt.hist(data, bins=300, density=True, alpha=0.6, color='g', label='SPY Histogram')



    plt.plot(x, pdf_fitted, 'k',color = 'r', label=dist_name, linewidth=2)
#title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
#plt.title(title)
    plt.legend()

    plt.show()
# Store distribution paraemters in a dataframe (this could also be saved)
dist_parameters = pd.DataFrame()
dist_parameters['Distribution'] = (
        results['Distribution'].iloc[0:number_distributions_to_plot])
dist_parameters['Distribution parameters'] = parameters

# Print parameter results
print ('\nDistribution parameters:')
print ('------------------------')

for index, row in dist_parameters.iterrows():
    print ('\nDistribution:', row[0])
    print ('Parameters:', row[1] )

#%%
