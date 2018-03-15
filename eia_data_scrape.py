# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
# BeautifulSoup, Pandas, and Requests/Splinter
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# Allows you to interact with chrome from python, just like a printer driver

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', headless=False)

# EIA browser to grab table
url = 'https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_06_a'
browser.visit(url)


# Grab table with pandas
table_list = pd.read_html(url)
table = table_list[1]


# Rename Table Columns
table.columns = ['State','Residential December 2017','Residential December 2016','Commercial December 2017', 'Commercial December 2016', \
             'Industrial December 2017', 'Industrial December 2016', 'Transportation December 2017', 'Transportation December 2016', \
             'All Sectors December 2017', 'All Sectors December 2016']


# Remove Regions from list
remove_list = ['U.S. Total', 'Mountain', 'New England','South Atlantic', 'Middle Atlantic', 'East North Central', 'West North Central', 'East South Central', 'West South Central', 'Pacific Contiguous', 'Pacific Noncontiguous']
states_table = table[~table.State.isin(remove_list)]

# Sort by State and reset index
states_table.sort_values(by=["State"], inplace = True)
states_table.reset_index(drop=True, inplace = True)
states_table.to_csv('csv/eia_data_scrape.csv')

