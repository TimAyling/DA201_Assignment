#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # Course 2: Data Analytics using Python

# ## Assignment: Diagnostic Analysis using Python
# 
# You’ll be working with real-world data to address a problem faced by the National Health Service (NHS). The analysis will require you to utilise Python to explore the available data, create visualisations to identify trends, and extract meaningful insights to inform decision-making. 

# ### A note for students using this template
# 
#  > ***Markdown*** Remember to change cell types to `Markdown`. You can review [Markdown basics](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) to find out how to add formatted text, links, and images to your notebook.

# # 

# # Assignment activity 1

# In[1]:


# My GitHub repository.


# In[ ]:


# https://github.com/TimAyling/DA201_Assignment/tree/main


# # 

# # Assignment activity 2

# ### Prepare your workstation

# In[1]:


# Import the necessary libraries.
import pandas as pd
import numpy as np

# Optional - Ignore warnings.
import warnings
warnings.filterwarnings('ignore')


# In[3]:


# Import and sense-check the actual_duration.csv data set as ad.
ad = pd.read_csv('actual_duration.csv')

# View the DataFrame
print(ad.shape)
ad.dtypes


# In[13]:


# Viewing the head of the DataFrame Actual Duration
ad.head(5)


# In[14]:


# Viewing the tail of the DataFrame Actual Duration
ad.tail(5)


# In[6]:


# Determine whether there are missing values.
ad_na = ad[ad.isna().any(axis=1)]

ad_na.shape


# In[12]:


# Determine the metadata of the data set.


# In[ ]:


# Determine the descriptive statistics of the data set.


# In[7]:


# Import and sense-check the appointments_regional.csv data set as ar.
ar = pd.read_csv('appointments_regional.csv')

# View the DataFrame
print(ar.shape)
print(ar.dtypes)


# In[15]:


# Viewing the head of the DataFrame Appointments Regional
ar.head(5)


# In[16]:


# Viewing the tail of the DataFrame Appointments Regional
ar.tail(5)


# In[8]:


# Determine whether there are missing values.
ar_na = ar[ar.isna().any(axis=1)]

ar_na.shape


# In[ ]:


# Determine the metadata of the data set.


# In[ ]:


# Determine the descriptive statistics of the data set.


# In[9]:


# Import and sense-check the national_categories.xlsx data set as nc.
nc = pd.read_excel('national_categories.xlsx')

# View the DataFrame
print(nc.shape)
nc.dtypes


# In[17]:


# Viewing the head of the DataFrame National Categories
nc.head(5)


# In[18]:


# Viewing the tail of the DataFrame National Categories
nc.tail(5)


# In[10]:


# Determine whether there are missing values.
nc_na = nc[nc.isna().any(axis=1)]

nc_na.shape


# In[ ]:


# Determine the metadata of the data set.


# In[ ]:


# Determine the descriptive statistics of the data set.


# ### Explore the data set

# **Question 1:** How many locations are there in the data set?

# In[ ]:


# Determine the number of locations.


# **Question 2:** What are the five locations with the highest number of records?
# 
# 

# In[ ]:


# Determine the top five locations based on record count.


# **Question 3:** How many service settings, context types, national categories, and appointment statuses are there?

# In[ ]:


# Determine the number of service settings.


# In[ ]:


# Determine the number of context types.


# In[ ]:


# Determine the number of national categories.


# In[ ]:


# Determine the number of appointment status.


# # 

# # Assignment activity 3

# ### Continue to explore the data and search for answers to more specific questions posed by the NHS.

# **Question 1:** Between what dates were appointments scheduled? 

# In[ ]:


# View the first five rows of appointment_date for the ad DataFrame to determine the date format.


# In[ ]:


# View the first five rows of appointment_date for the nc DataFrame to determine the date format.


# In[ ]:


# Change the date format of ad['appointment_date'].


# View the DateFrame.


# In[ ]:


# Change the date format of ar['appointment_date'].


# View the DateFrame.


# In[ ]:


# Determine the minimum and maximum dates in the ad DataFrame.
# Use appropriate docstrings.


# In[ ]:


# Determine the minimum and maximum dates in the nc DataFrame.
# Use appropriate docstrings.


# **Question 2:** Which service setting was the most popular for NHS North West London from 1 January to 1 June 2022?

# In[ ]:


# For each of these service settings, determine the number of records available for the period and the location. 


# View the output.


# **Question 3:** Which month had the highest number of appointments?

# In[ ]:


# Number of appointments per month == sum of count_of_appointments by month.
# Use the groupby() and sort_values() functions.


# **Question 4:** What was the total number of records per month?

# In[ ]:


# Total number of records per month.


# # 

# # Assignment activity 4

# ### Create visualisations and identify possible monthly and seasonal trends in the data.

# In[ ]:


# Import the necessary libraries.
import seaborn as sns
import matplotlib.pyplot as plt

# Set figure size.
sns.set(rc={'figure.figsize':(15, 12)})

# Set the plot style as white.
sns.set_style('white')


# ### Objective 1
# Create three visualisations indicating the number of appointments per month for service settings, context types, and national categories.

# In[ ]:


# Change the data type of the appointment month to string to allow for easier plotting.


# In[ ]:


# Aggregate on monthly level and determine the sum of records per month.


# View output.


# **Service settings:**

# In[ ]:


# Plot the appointments over the available date range, and review the service settings for months.
# Create a lineplot.


# **Context types:**

# In[ ]:


# Create a separate data set that can be used in future weeks. 


# View output.


# In[ ]:


# Plot the appointments over the available date range, and review the context types for months.
# Create a lineplot.


# **National categories:**

# In[ ]:


# Create a separate data set that can be used in future weeks. 


# View output.


# In[ ]:


# Plot the appointments over the available date range, and review the national categories for months.
# Create a lineplot.


# ### Objective 2
# Create four visualisations indicating the number of appointments for service setting per season. The seasons are summer (August 2021), autumn (October 2021), winter (January 2022), and spring (April 2022).

# **Summer (August 2021):**

# In[ ]:


# Create a separate data set that can be used in future weeks. 


# View output.


# In[ ]:


# Look at August 2021 in more detail to allow a closer look.
# Create a lineplot.


# **Autumn (October 2021):**

# In[ ]:


# Look at October 2021 in more detail to allow a closer look.
# Create a lineplot.


# **Winter (January 2022):**

# In[ ]:


# Look at January 2022 in more detail to allow a closer look.
# Create a lineplot.


# **Spring (April 2022):**

# In[ ]:


# Look at April 2022 in more detail to allow a closer look.
# Create a lineplot.


# # 

# # Assignment activity 5

# ### Analyse tweets from Twitter with hashtags related to healthcare in the UK.

# In[ ]:


# Libraries and settings needed for analysis
import pandas as pd
import seaborn as sns

# Set figure size.
sns.set(rc={'figure.figsize':(15, 12)})

# Set the plot style as white.
sns.set_style('white')

# Maximum column width to display
pd.options.display.max_colwidth = 200


# In[ ]:


# Load the data set.


# View the DataFrame.


# In[ ]:


# Explore the metadata.


# In[ ]:


# Explore the data set.


# In[ ]:


# Would it be useful to only look at retweeted and favourite tweet messages?
# Explain your answer.


# In[ ]:


# Create a new DataFrame containing only the text.


# View the DataFrame.


# In[ ]:


# Loop through the messages, and create a list of values containing the # symbol.


# In[ ]:


# Display the first 30 records.


# In[ ]:


# Convert the series to a DataFrame in preparation for visualisation.


# Rename the columns.


# In[ ]:


# Fix the count datatype.


# View the result.


# In[ ]:


# Display records where the count is larger than 10.


# In[ ]:


# Create a Seaborn barplot indicating records with a count >10 records.


# In[ ]:


# Create the plot.


# View the barplot.


# # 

# # Assignment activity 6

# ### Investigate the main cencerns posed by the NHS. 

# In[ ]:


# Prepare your workstation.
# Load the appointments_regional.csv file.


# View the DataFrame.


# In[ ]:


# Print the min and max dates.


# In[ ]:


# Filter the data set to only look at data from 2021-08 onwards.


# **Question 1:** Should the NHS start looking at increasing staff levels? 

# In[ ]:


# Create an aggregated data set to review the different features.


# View the DataFrame.


# In[ ]:


# Determine the total number of appointments per month.


# Add a new column to indicate the average utilisation of services.
# Monthly aggregate / 30 to get to a daily value.


# View the DataFrame.


# In[ ]:


# Plot sum of count of monthly visits.
# Convert the appointment_month to string data type for ease of visualisation.


# Create a lineplot with Seaborn.


# In[ ]:


# Plot monthly capacity utilisation.


# Create a lineplot.


# **Question 2:** How do the healthcare professional types differ over time?

# In[ ]:


# Create a line plot to answer the question.


# **Question 3:** Are there significant changes in whether or not visits are attended?

# In[ ]:


# Create a line plot to answer the question.


# **Question 4:** Are there changes in terms of appointment type and the busiest months?

# In[ ]:


# Create a line plot to answer the question.


# **Question 5:** Are there any trends in time between booking an appointment?

# In[ ]:


# Create a line plot to answer the question.


# **Question 6:** How do the spread of service settings compare?

# In[ ]:


# Let's go back to the national category DataFrame you created in an earlier assignment activity.


# In[ ]:


# Create a new DataFrame consisting of the month of appointment and the number of appointments.

# View the DataFrame.


# In[1]:


# Create a boxplot to investigate spread of service settings.


# In[ ]:


# Create a boxplot to investigate the service settings without GP.


# # 

# ### Provide a summary of your findings and recommendations based on the analysis.

# In[ ]:




