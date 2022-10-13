#!/usr/bin/env python
# coding: utf-8

# In[37]:


# Import the necessary packages
import pandas as pd

# Import the national categories data set
cat = pd.read_excel('national_categories.xlsx')

# View the DataFrame
print(cat.shape)
cat.dtypes


# In[38]:


# Viewing the head of the DataFrame National Categories
cat.head(5)


# In[39]:


# Viewing the head of the DataFrame National Categories
cat.tail(5)


# In[34]:


# Import the regional appointment data set
r_app = pd.read_csv('appointments_regional.csv')

# View the DataFrame
print(r_app.shape)
print(r_app.dtypes)


# In[35]:


# Viewing the head of the DataFrame Regional Appointment
r_app.head(5)


# In[40]:


# Viewing the tail of the DataFrame Actual Duration
r_app.tail(5)


# In[31]:


# Import the actual duration data set
dur1 = pd.read_csv('actual_duration.csv')

# View the DataFrame
print(dur1.shape)
dur1.dtypes


# In[32]:


# Viewing the head of the DataFrame Actual Duration
dur1.head(5)


# In[33]:


# Viewing the tail of the DataFrame Actual Duration
dur1.tail(5)


# In[26]:


# Import the tweets data set
tweets1 = pd.read_csv('tweets.csv')

# Shape of the DataFrame
print(tweets1.shape)
print(tweets1.dtypes)


# In[29]:


# Viewing the head of the DataFrame
tweets1.head(5)


# In[30]:


# Viewing the tail of the DataFrame
tweets1.tail(5)


# In[ ]:




