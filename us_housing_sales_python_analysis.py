#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[17]:


df=pd.read_csv("C:/Users/sirvi/OneDrive/Desktop/US HOUSING SALES MAIN FILE.csv") 
#FILE UPLOAD


# In[12]:


df.info()


# In[18]:


df.shape


# # the data has 21613 rows and 30 columns

# In[14]:


pd.isnull(df)


# # no null data found

# In[15]:


df.columns


# # DATA CLEANING ,BINNING,INTEGRATION COMPLETES HERE.

# In[ ]:





# # EDA-EXPLORATORY DATA ANALYSIS

# In[ ]:





# In[19]:


df[['price','bedrooms']].describe()


# # 1. SALE AS PER PRICE RANGE--
# 
# 200000 TO 1200000 USD HAS THE MOST NUMBER OF SALES ,WHILE 2500000 $ HAS THE LEAST NO OF SALES.

# In[ ]:





# In[20]:


bx=sns.countplot(x = 'price_RANGE',data=df)
for bars in bx.containers:
    bx.bar_label(bars)


# In[ ]:





# # 2.SALE AS PER BEDROOMS-
#  
# MOST PEOPLE PREFER 1-3 BEDROOMS WHILE LUXURY ONES HAVING MORE THAN 7 BEDROOMS HAVE VERY FEW SALES i.e 62
# 

# In[22]:


bx=sns.countplot(x ='BEDROOM_RANGE' ,data=df)
for bars in bx.containers:
    bx.bar_label(bars)


# In[ ]:





# In[23]:


df.columns


# In[ ]:





# # 3.SALE AS PER SQ_FT LIVING AREA- PEOPLE MOSTLY PREFER 1K-5K SQUARE FEET LIVING AREA
# 

# In[24]:


bx=sns.countplot(x = 'sqft_living_AREA',data=df)
for bars in bx.containers:
    bx.bar_label(bars)


# In[ ]:





# # 4. SALE AS PER  SQ_FEET PRICE- PEOPLE USUALLY PREFER TO BUY AT 2000 TO 10000 USD.
# 

# In[25]:


bx=sns.countplot(x ='sqft_lot_CATEGORICAL'
,data=df)
for bars in bx.containers:
    bx.bar_label(bars)


# In[ ]:





# # 5.SALE AS PER CATEGORICAL- PEOPLE USED TO BUY THE MID_TERM CATEGORY FLATS MORE THAN THE HIGH CATEGORY FLATS.
# 

# In[ ]:





# In[28]:


df.columns


# In[ ]:





# In[ ]:





# In[29]:


bx=sns.countplot(x ='condition' ,data=df)
for bars in bx.containers:
    bx.bar_label(bars)


# In[ ]:





# # 6 PEOPLE LOVE TO BUY HOUSES WHICH IS IN ITS ORGANIC FORM

# In[ ]:





# In[30]:


bx=sns.countplot(x ='yr_renovated_CATEGORICAL' ,data=df)
for bars in bx.containers:
    bx.bar_label(bars)


# In[ ]:





# # 7. NO BASEMENT FLAT HAVE BETTER SALES REPRESENTATIVE AS THEY ARE CHEAPER AND AFFORDABLE
# 

# In[31]:


bx=sns.countplot(x = 'sqft_basement_CATEGORICAL',data=df)
for bars in bx.containers:
    bx.bar_label(bars)


# In[ ]:





# # --------the end-----

# In[ ]:





# In[ ]:





# In[ ]:




