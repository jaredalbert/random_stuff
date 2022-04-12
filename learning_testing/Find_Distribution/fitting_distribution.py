# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:49:00 2020

"""

import pandas as pd
import numpy as np
import scipy
from sklearn.preprocessing import StandardScaler
import scipy.stats
import matplotlib.pyplot as plt
#%matplotlib inline
# Load data and select first column

from sklearn import datasets
path_spy='C:/Users/jaredalbert/Desktop/python_scripts/IPO_study/SPY.csv'



df = pd.read_csv(path_spy, parse_dates=True)
df['Date']=pd.to_datetime(df['Date'])
df = df.set_index(df['Date'])
df['ln_change'] = (np.log(df['Adj Close']/df['Adj Close'].shift(1)))
df.ln_change.dropna(inplace=True)

y=np.array(df.ln_change)
df['ln_change']

x = np.arange(len(y))
size = len(y)

ds_df = pd.DataFrame(y, columns = ['LN_change'])
ds_df.describe()
plt.hist(y, bins = 100)
plt.show()

sc=StandardScaler()
yy = y.reshape (-1,1)
sc.fit(yy)
y_std =sc.transform(yy)
y_std = y_std.flatten()
#y_std.shape
pd.DataFrame(y_std).describe()
#sc.n_samples_seen_
import warnings
warnings.filterwarnings("ignore")
#%%
d = 'alpha, anglit, arcsine, argus, beta, betaprime, bradford, burr, burr12, \
cauchy, chi, chi2, cosine, crystalball, dgamma, dweibull, erlang, \
expon, exponnorm, exponweib, exponpow, f, fatiguelife, fisk, foldcauchy, \
foldnorm, frechet_r, genlogistic, gennorm, genpareto, genexpon, \
genextreme, gausshyper, gamma, gengamma, genhalflogistic, \
gilbrat, gompertz, gumbel_r, gumbel_l, halfcauchy, halflogistic, \
halfnorm, halfgennorm, hypsecant, invgamma, invgauss, invweibull, \
johnsonsb, johnsonsu, kappa4, kappa3, ksone, kstwobign, laplace, \
levy, levy_l, logistic, loggamma, loglaplace, lognorm, \
lomax, maxwell, mielke, moyal, nakagami, ncx2, ncf, nct, \
norm, norminvgauss, pareto, pearson3, powerlaw, powerlognorm, powernorm, \
rdist, rayleigh, rice, recipinvgauss, semicircular, skewnorm, t, trapz, \
triang, truncexpon, truncnorm, tukeylambda, uniform, vonmises, \
vonmises_line, wald, weibull_min, weibull_max, wrapcauchy'.split(', ')


#%%

chi_square = []
p_values = []

percentile_bins = np.linspace(0,100,51)
percentile_cutoffs = np.nanpercentile(y_std, percentile_bins)
observed_frequency, bins = (np.histogram(y_std, bins=percentile_cutoffs))
cum_observed_frequency = np.cumsum(observed_frequency)

for distribution in d:
    # Set up distribution and get fitted distribution parameters
    dist = getattr(scipy.stats, distribution)
    param = dist.fit(y_std)

    # Obtain the KS test P statistic, round it to 5 decimal places
    p = scipy.stats.kstest(y_std, distribution, args=param)[1]
    p = np.around(p, 5)
    p_values.append(p)


    # Get expected counts in percentile bins
    # This is based on a 'cumulative distrubution function' (cdf)
    cdf_fitted = dist.cdf(percentile_cutoffs, *param[:-2], loc=param[-2],
                          scale=param[-1])
    expected_frequency = []
    for bin in range(len(percentile_bins)-1):
        expected_cdf_area = cdf_fitted[bin+1] - cdf_fitted[bin]
        expected_frequency.append(expected_cdf_area)

    # calculate chi-squared
    expected_frequency = np.array(expected_frequency) * size
    cum_expected_frequency = np.cumsum(expected_frequency)
    ss = sum (((cum_expected_frequency - cum_observed_frequency) ** 2) / cum_observed_frequency)
    ss = np.around(ss, decimals = 0)
    chi_square.append(ss)

# Collate results and sort by goodness of fit (best at top)

results = pd.DataFrame()
results['Distribution'] = d
results['chi_square'] = chi_square
results['p_value'] = p_values
results.sort_values(['chi_square'], inplace=True)

# Report results

print ('\nDistributions sorted by goodness of fit:')
print ('----------------------------------------')
print (results)

