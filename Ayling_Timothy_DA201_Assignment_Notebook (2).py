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


# In[62]:


# Data imported correctly?
print(cat.columns)


# In[38]:


# Viewing the head of the DataFrame National Categories
cat.head(5)


# In[39]:


# Viewing the head of the DataFrame National Categories
cat.tail(5)


# In[41]:


# Check for missing values National Categories
cat_na = cat[cat.isna().any(axis=1)]

cat_na.shape


# In[48]:


# Number of locations  -i.e. sub_icb_location_name
# Create a group and then determine its size
loc_name = cat.groupby('sub_icb_location_name')
loc_name.size()


# In[49]:


# Number of locations  -i.e. service_setting
# Create a group and then determine its size
service_set = cat.groupby('service_setting')
service_set.size()


# In[50]:


# Number of locations  -i.e. context_type
# Create a group and then determine its size
con_type = cat.groupby('context_type')
con_type.size()


# In[51]:


# Number of locations  -i.e. national_category
# Create a group and then determine its size
nat_category = cat.groupby('national_category')
nat_category.size()


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


# Viewing the tail of the DataFrame Regional Appointment
r_app.tail(5)


# In[46]:


# Check for missing values Regional Appointment
r_app_na = r_app[r_app.isna().any(axis=1)]

r_app_na.shape


# In[61]:


# Number of attendance  -i.e. appointment_status
# Create a group and then determine its size
attendance_r_app = r_app.groupby(['appointment_status'])['Unknown'].count()
print(attendance_r_app)


# In[ ]:





# In[ ]:





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


# In[44]:


# Check for missing values Actual Duration
dur1_na = dur1[cat.isna().any(axis=1)]

dur1_na.shape


# In[26]:


# Import the tweets data set
tweets1 = pd.read_csv('tweets.csv')

# Shape of the DataFrame
print(tweets1.shape)
print(tweets1.dtypes)


# In[29]:


# Viewing the head of the DataFrame Tweets
tweets1.head(5)


# In[30]:


# Viewing the tail of the DataFrame Tweets
tweets1.tail(5)


# In[43]:


# Check for missing values Tweets
tweets1_na = tweets1[cat.isna().any(axis=1)]

tweets1_na.shape


# In[ ]:




