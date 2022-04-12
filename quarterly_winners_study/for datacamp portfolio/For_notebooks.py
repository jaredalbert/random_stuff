# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 18:39:15 2021

@author: Windows10
"""
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta
#import seaborn as sns

pd.set_option('display.max_columns', None)

tickers = pd.read_csv('C:/Users/Windows10/Desktop/from old dell/Python_files/quarterly_winners_study/for datacamp portfolio/stock_final_1.csv')


#%%

#print(tickers.head())                     
tickers.Date = pd.to_datetime(tickers.Date)
tickers['Offset_Date']=tickers.Date + timedelta(days=0)
tickers.set_index('Offset_Date', inplace=True)

q_tickers = tickers.groupby('Name').resample('Q').last()



#%%
pd.options.mode.chained_assignment = None  # default='warn'

df =q_tickers.drop(['Name'], axis = 1).reset_index()
df.drop(columns = ['Low', 'High', 'Close', 'Open', 'Volume'], inplace = True)

#%%
stats = {}
df_4 =pd.DataFrame()
symbols = set(q_tickers['Name'])
for s in symbols:
    df_sym = df[df['Name']==str(s)]
    for i in range(-1,5):
        df_sym['ln_ret_' + str(i)] = np.log(df_sym['Adj Close']/df_sym['Adj Close'].shift(i)).shift(-i)
        #print(df_sym)
        m = np.mean(df_sym['ln_ret_' + str(i)])
        if i<0:    #needed to make the -q positive for rise and negative for fall to match q0 to q1
            m*=-1
        sd = np.std(df_sym['ln_ret_' + str(i)])
        stats[str(s) + '_' + str(i)] = (m, sd)
    df_4 =df_4.append(pd.DataFrame(df_sym))
df_4['ln_ret_-1']=df_4['ln_ret_-1'] * -1  #Needed to make the -q positive for rise and negative for fall to match q0 to q1
#df_4.drop('ln_ret_0',axis =1, inplace=True) #These were all changes with self so 0's
        #print(str(df_sym['Name'] + '_' + str(i)))
#%%
df_4.reset_index(inplace = True)
df_4.drop('index', axis =1, inplace=True)

bins, steps = 10, .1
df_5 = df_4['ln_ret_-1'].quantile(np.arange(0,int(bins*steps),steps)).reset_index()
levels, vals =[], []
for i in range(bins):
    levels.append(df_5['ln_ret_-1'].iloc[i])
for i in range(bins):
    if i+1 in range(bins):
        lower = df_4['ln_ret_-1']>=levels[i]  
        upper = df_4['ln_ret_-1']<=levels[i+1]
    else:
        lower = df_4['ln_ret_-1']>=levels[i] 
        upper = True
    x = df_4[lower & upper]
    vals.append((x['ln_ret_-1'].mean(),x['ln_ret_1'].mean(),x['ln_ret_2'].mean(),  \
          x['ln_ret_3'].mean(),x['ln_ret_4'].mean()))
df_6=pd.DataFrame(vals)
#%%
#smallest = ((df_4['ln_ret_-1']>=levels[0])  & (df_4['ln_ret_-1']<=levels[1]))
'''The change over the first quarter is the most dramatic.
 I'll use the two sided t-test and p-test to make see if the change is significant'''
from scipy import stats
worst = df_4[((df_4['ln_ret_-1']>=levels[0])  & (df_4['ln_ret_-1']<=levels[1]))]['ln_ret_1'].dropna()
best = df_4[df_4['ln_ret_-1']>=levels[-1]]['ln_ret_1'].dropna()
print(stats.ttest_ind(worst, best, equal_var=False))
#Ttest_indResult(statistic=10.041715104683767, pvalue=3.7259742169101605e-23)


#%%
#fig, ax = plt.subplot()
fig, ax = plt.subplots(figsize=(10,10))
fig.suptitle('Return of quantile over the next 4 quarters', fontsize=25)
ax.set_xlabel('Quarters', fontsize=20)
ax.set_ylabel('Ln return', fontsize=20)
df_6.T.plot(ax=ax, xticks=([0,1,2,3,4]))
#plt.show()
#%%

'''the effect is real, is it only end of year to end of first quarter
or is it even across quarters?'''
df_4.groupby(df_4.Date.dt.month).mean()
worst_s = df_4[((df_4['ln_ret_-1']>=levels[0])  & (df_4['ln_ret_-1']<=levels[1]))][['Date','ln_ret_1']].dropna()
best_s = df_4[df_4['ln_ret_-1']>=levels[-1]][['Date','ln_ret_1']].dropna()
worst_by_q = worst_s.groupby(worst_s['Date'].dt.month).mean()
best_by_q = best_s.groupby(best_s['Date'].dt.month).mean()
'''does seems to be a very strong enod of year and also christmas rally which is surprising'''
#%%

#df_4[[df_4['ln_ret_-1']>=levels[1]  and df_4['ln_ret_-1']<=levels[2]]]
# for i in range(bins):
#     lower = df_4['ln_ret_-1']>=levels[i-1]  
#     upper = df_4['ln_ret_-1']<=levels[i]
#     x = df_4[lower & upper]
#     vals.append((x['ln_ret_-1'].mean(),x['ln_ret_1'].mean(),x['ln_ret_2'].mean(),  \
#           x['ln_ret_3'].mean(),x['ln_ret_4'].mean()))
# df_6=pd.DataFrame(vals)



#df_4=pd.DataFrame(l, columns=columns)

#%%
'''
num_cases = sorted(list({str(k)[-2:] for k in stats.keys()}))

   
gen=[(str(k)[-2:], v[0],v[1]) for k,v in stats.items()]
#study_df = pd.DataFrame(gen, columns = num_cases)
study_df=pd.DataFrame(gen, columns = ['ln_change', 'mean','std'])
df_3b = study_df.groupby('ln_change').agg({'mean':'mean', 'std':'mean'})
df_3 = study_df.groupby('ln_change').quantile(q=np.linspace(0,1,10))
df_3a = study_df.groupby('ln_change').quantile(q=np.linspace(0,1,10)).agg({'mean':'mean', 'std':'mean'})
df_3.reset_index(inplace=True)
levels = df_3[df_3['ln_change']=='-1']
#%%
#df_4[df_4['ln_ret_-1'] <= levels.iloc[0]['mean']]
m = study_df[study_df['ln_change']=='-1']['mean']
s = study_df[study_df['ln_change']=='-1']['std']




#study_df.mask('ln_change'==1, 'mean'*-1, inplace=True)
#study_df.where(study_df['ln_change']=='-1', study_df['mean']*-1, inplace=True, axis =0)
#study_df['new_mean']=study_df.loc[study_df['ln_change']=='-1']['mean'] * -1

#study_df[study_df['ln_change']=='-1']['mean']*-1 #needed to make the -1 q positive for rise and negative for fall
#study_df['ln_change'] = study_df['ln_change'].astype('int')

#means = study_df.groupby('ln_change')['mean_std'][0].mean()
'''

#%%
# for k,v in stats.items():
    
#     one.append((str(k)[-1], v))
    

  
# for k, v in stats.items():
#     print(str(k)[-1], v[0])

    
   # df+str(s) = df[df['Name']=='A']
#df_a['ln_ret_1'] = np.log(df_a['Adj Close']/df_a['Adj Close'].shift(1)).shift(-1)

#%%'''
'''df['ln_ret_1'] = np.log(df['Adj Close']/df['Adj Close'].shift(1)).shift(-1)
    
df['x'] = df['Name'] == df['Name'].shift(-1)
for i in range(df.shape[0]):
    if df['x'].loc[i]==True:
        df['ln_ret_1_a']= df['ln_ret_1'][i] 
   # else:
   #     df['ln_ret_1'].loc[i] = False
       
# if df['x']:
#     df['ln_ret_1'] = np.log(df['Adj Close']/df['Adj Close'].shift(1)).shift(-1)
# else:
#     df['ln_ret_1'] = None

df['pct_ret_1'] = df['Adj Close'].pct_change(1).shift(-1)
df['ln_ret_1'] = np.log(df['Adj Close']/df['Adj Close'].shift(1)).shift(-1)


#%%

y=df.groupby(['Name', 'Date'])['Name', 'Date', 'Adj Close']
y['ln_ret_1'] = np.log(y['Adj Close'])/np.log(y['Adj Close'].shift(1))




#%%
q_tickers['log_ret_0'] = np.log(q_tickers['Adj Close']/q_tickers['Adj Close'].shift(1))
for i in range(1,5):    
    q_tickers['log_ret' +'_' + str(i)] = np.log(q_tickers['Adj Close'].shift(-i)/q_tickers['Adj Close'])
#q_tickers.drop('Name', axis= 1, inplace=True)
#q_tickers.reset_index('Name', inplace=True)
q_dates = sorted(str(item)[:10] for item in list(set(q_tickers.index)))
#%%
df_losers = pd.DataFrame()
df_winners = pd.DataFrame()

#pd.qcut(df['NormRange'], 10,labels= np.arange(1,11))
#q1_rank = q_tickers.loc['2016-09-30'].groupby('log_ret_0').last()
#losers = q1_rank.head(q1_rank.shape[0]//10)
#df_losers = df_losers.append(losers)
for date in q_dates[1:-4]:
    q1_rank = q_tickers.loc[date].groupby('log_ret_0').last()
    
    losers = q1_rank.head(q1_rank.shape[0]//10)
    df_losers = df_losers.append(losers)

    winners = q1_rank.tail(q1_rank.shape[0]//10)
    df_winners = df_winners.append(winners)

cols = ['log_ret_1', 'log_ret_2', 'log_ret_3', 'log_ret_4']
def sum_stats(val):
    mean = np.round(np.mean(val),3)
    sd = np.round(np.std(val),3)
    n = len(val)
    t_stat = np.round(mean/(sd/np.sqrt(n)),2)
    #print (f' mean: {mean},  stdev: {sd}, count: {n}, t-stat: {t_stat}')
    return (mean, sd, n, t_stat)
losers_results, winners_results =[],[]
for col in cols:
    #print(f'loser: {col}')
    res_l = sum_stats(df_losers[col])
    losers_results.append(res_l)
    #print(f'winner: {col}')
    res_w = sum_stats(df_winners[col])
    winners_results.append(res_w)
l = pd.DataFrame(losers_results, index = cols, columns = ('mean', 'stdev', 'count', 't_stat'))
w = pd.DataFrame(winners_results, index = cols, columns = ('mean', 'stdev', 'count', 't_stat'))  

####winners
print (sum_stats(df_winners.reset_index()['log_ret_0']))
####losers
print (sum_stats(df_losers.reset_index()['log_ret_0']))
# sns.histplot(df_winners['log_ret_4'],kde=False, color='red', bins=100)
# plt.show()

'''