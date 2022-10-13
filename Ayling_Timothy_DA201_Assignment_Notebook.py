#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the necessary packages
import pandas as pd


# In[ ]:


# Import the national categories data set
cat = pd.read_excel('national_categories.xlsx')

# View the DataFrame
cat.head()
cat.tail()
cat.shape()
print(cat.dtypes)


# In[ ]:


# Import the regional appointment data set
r_app = pd.read_csv('appointments_regional.csv')

# View the DataFrame
r_app.head()
r_app.tail()
r_app.shape()
print(r_app.dtypes)


# In[ ]:


# Import the tweets data set
tweets1 = pd.read_csv('tweets.csv')

# View the DataFrame
tweets1.head()
tweets1.tail()
tweets1.shape()
print(tweets1.dtypes)


# In[ ]:


# Import the actual duration data set
dur1 = pd.read_csv('actual_duration.csv')

# View the DataFrame
dur1.head()
dur1.tail()
dur1.shape()
dur1.dtypes


# In[ ]:




