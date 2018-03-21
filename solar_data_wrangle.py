
# coding: utf-8

# In[1]:


# dependencies
import pandas as pd
import numpy as np

from sqlalchemy import create_engine


# In[2]:


# read cancercsv into dataframe
cancer_df = pd.read_csv("static/csv/skin_map_incidence.csv")
cancer_df.head()


# In[3]:


# read solar install csv into dataframe
solar_df = pd.read_csv("static/csv/openpv-export-201803141836.csv")
solar_df.head(2)


# In[4]:


solar_targs_df = solar_df.iloc[:,[0, 1, 4, 6, 9]]
solar_targs_df.columns = ["state", "install_Data", "size_kw", "zip", "cost_per_Watt"]
solar_targs_df.head(2)


# In[5]:


# check to see how deeply the nans permiate our data
solar_targs_df.count()


# In[6]:


# read eia cost data into dataframe
eia_df = pd.read_csv("static/csv/eia_2014_scrape.csv")
eia_df = eia_df.iloc[:,[1,2]]
eia_df["State"] = ["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS",
                   "KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC",
                   "ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
# eia_df


# In[7]:


# merge cancer and electric cost dfs
cande_df = pd.merge(cancer_df, eia_df, on="State", how="outer")
cande_df.columns = ["state", "range", "rate", "name", "average retail price (cents/kWh)"]
electric_cancer = cande_df[["name","state","rate","average retail price (cents/kWh)"]]
electric_cancer.columns = ["state","sbbr","cancer_Rate","electric_Cost"]
#electric_cancer.head()
electric_cancer.to_csv("static/csv/electric_cost_cancer_rate.csv")


# In[17]:


# merge solar and cande dfs
data_df = pd.merge(cande_df, solar_targs_df, on="state", how="outer")

# reset index to serve as id column
data_df = data_df.reset_index()
#data_df.head()

# rename columns and reorder columns
data_df.columns = ["id", "abbr", "c_range", "cancer_Rate", "state", "electric_Cost_cents_kWh)", "install_Date",
                  "size_kW", "zipcode", "cost_per_Watt"]
data_df = data_df[["id", "state", "abbr", "electric_Cost_cents_kWh)", "install_Date", "zipcode", "size_kW",
                 "cost_per_Watt", "c_range", "cancer_Rate"]]
data_df["size_kW"].fillna(0, inplace=True)
#data_df.head(10)

# push clean df to csv
data_df.to_csv("static/csv/clean_data.csv")


# In[9]:


one = []

for i in data_df["size_kW"]:
    i == data_df["size_kW"]
    if 0 < i < 10:
        one.append(i)
    else :
        one.append(0)

two = []
for i in data_df["size_kW"]:
    i == data_df["size_kW"]
    if 10 <= i < 100:
        two.append(i)
    else :
        two.append(0)

three = []
for i in data_df["size_kW"]:
    i == data_df["size_kW"]
    if i >= 100:
        three.append(i)
    else :
        three.append(0)

data_df["size_one"] = one
data_df["size_two"] = two
data_df["size_three"] = three

#data_df.head(50)


# In[10]:


# create df with total installed kW by state
installed = data_df.groupby(["state", "abbr"])["size_kW", "size_one", "size_two", "size_three"].sum()
installed_df = pd.DataFrame(installed)
installs_df = installed_df.reset_index()
# installs_df
installs_df.to_csv("static/csv/install_totals_state.csv")


# In[11]:


install_groups = installs_df.drop("size_kW", axis=1)
install_groups.head()
install_groups.to_csv("static/csv/install_groups_state.csv")


# In[12]:


installs_ecost = installs_df
installs_ecost["electric_cost"] = electric_cancer["electric_Cost"]
# installs_ecost
installs_ecost.to_csv("static/csv/installs_ecost.csv")


# In[13]:


data_df.drop("size_one", axis=1, inplace=True)
data_df.drop("size_two", axis=1, inplace=True)
data_df.drop("size_three", axis=1, inplace=True)
#data_df.head()


# In[14]:


# push data to sqlite db
engine = create_engine('sqlite:///clean_solar_data.db')
data_df.to_sql("data", con=engine, flavor="sqlite", if_exists="replace", index=False)
installs_df.to_sql("install_total", con=engine, flavor="sqlite", if_exists="replace", index=False)
electric_cancer.to_sql("electric_cancer", con=engine, flavor="sqlite", if_exists="replace", index=False)
installs_ecost.to_sql("installs_ecost", con=engine, flavor="sqlite", if_exists="replace", index=False)


# In[23]:


# test db completion
df = pd.read_sql_query("SELECT * FROM 'installs_ecost'", engine)
df.head()


# In[60]:


#Setup datframes of top 10 sorted lists to include the state name, abbreviation, and metric; reset index

df_totalkw = df.sort_values(by=['size_kW'], ascending = False).head(n=10).iloc[:,0:3].reset_index(drop = True)
df_small= df.sort_values(by=['size_one'], ascending = False).head(n=10).loc[:,["state","abbr","size_one"]].reset_index(drop = True)
df_medium = df.sort_values(by=['size_two'], ascending = False).head(n=10).loc[:,["state","abbr","size_two"]].reset_index(drop = True)
df_large = df.sort_values(by=['size_three'], ascending = False).head(n=10).loc[:,["state","abbr","size_three"]].reset_index(drop = True)
df_cost = df.sort_values(by=['electric_cost'], ascending = False).head(n=10).loc[:,["state","abbr","electric_cost"]].reset_index(drop = True)


# In[62]:


#push files to csv

df_totalkw.to_csv('/static/csv/total_kw_table.csv',index_label = "Rank")
df_small.to_csv('/static/csv/small_kw_table.csv',index_label = "Rank")
df_medium.to_csv('/static/csv/medium_kw_table.csv',index_label = "Rank")
df_large.to_csv('/static/csv/large_kw_table.csv',index_label = "Rank")
df_cost.to_csv('/static/csv/elec_cost_table.csv',index_label = "Rank")

