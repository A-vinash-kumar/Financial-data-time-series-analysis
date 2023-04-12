#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Data being used - "GOOG Data from 2001 to 2018" to study price variations based on months

# Procedure :- Write the code to regroup the data by months and do calculations and compare

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()


# In[15]:


# STEP 1 :- Specify date range analysis
start = dt.datetime(2001,1,1)
end = dt.datetime(2018,1,1)
start,end


# In[16]:


# STEP 1 :- Specify date range analysis
start_date = '2001-01-01'
end_date = '2018-01-01'
start_date,end_date 


# In[4]:


# STEP 2 :- Creating file for future reference

SRC_DATA_FILENAME = 'goog_data_large.pkl'

try:
    goog_data = pd.read_pickle(SRC_DATA_FILENAME)
    print('File data not found ... reading GOOG data')
except FileNotFoundError:
    print('FIle not found ... downloading the GOOG data')


# In[17]:


# STEP 3 :- Creating GOOG dataframe

# Select stocks you would like to analyse
stocklist = ['GOOG']
stocks = stocklist

# Call the pandas_DataReader Datareader module:

# 2 ways of doing this:

# 1.   pdr.DataReader(stocks,'yahoo',start,end)
# 2.   pdr.get_data_yahoo(stocks,start,end)

goog_data=pdr.get_data_yahoo('GOOG',start_date,end_date)
goog_data.head()
goog_data.tail()


# In[18]:


# STEP 4 :- saving the GOOG dataframe

goog_data.to_pickle(SRC_DATA_FILENAME)


# In[24]:


#  STEP 5 :- Processing the data

# 1. Grouping data by month
goog_monthly_return = goog_data['Adj Close'].pct_change().groupby([goog_data['Adj Close'].index.year,goog_data['Adj Close'].index.month]).mean()


# Creating monthly return list holder
goog_monthly_return_list=[]

# Defining logic for individual data to put into list to make it dynamic
for i in range (len(goog_monthly_return)):
    goog_monthly_return_list.append({'month':goog_monthly_return.index[i][1],'monthly_return':goog_monthly_return[i]})
    
goog_monthly_return_list = pd.DataFrame(goog_monthly_return_list,columns = ('month','monthly_return'))


# In[9]:


#  STEP 6 :- Visualising the data

goog_monthly_return_list.boxplot(column = 'monthly_return',by = 'month')

ax = plt.gca()
labels = [item.get_text() for item in ax.get_xticklabels()]
labels = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
ax.set_xticklabels(labels)
ax.set_ylabel('GOOG return')
plt.tick_params(axis = 'both', which = 'major', labelsize = 7)
plt.title("GOOG Monthly return 2001-2018")
plt.suptitle("")
plt.show()

