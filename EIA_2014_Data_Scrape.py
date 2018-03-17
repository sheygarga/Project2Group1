
# coding: utf-8

# In[1]:


# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
# BeautifulSoup, Pandas, and Requests/Splinter
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


# In[2]:


# EIA browser to grab table
url = 'https://www.eia.gov/electricity/state/archive/2014/'


# In[3]:


# Grab table with pandas

table_list = pd.read_html(url)
table = table_list[0]
table.head()


# In[4]:


# Remove total row from list

remove_list = ['U.S. Total']
states_table = table[~table.Name.isin(remove_list)]

# remove non-price columns
ecost_df = states_table.iloc[:,[0,1]]

# push to csv
ecost_df.to_csv('csv/eia_2014_scrape.csv')
ecost_df

