#!/usr/bin/env python
# coding: utf-8

# In[48]:


pip install dataframe_image


# In[50]:


import pandas as pd
import numpy as np
import dataframe_image as dfi


# In[5]:


emails_csv = pd.read_csv('EMAILS.csv', sep = ";")
emails_csv


# In[7]:


emailsdataframe = pd.DataFrame(emails_csv)
emailsdataframe


# In[9]:


emails = emailsdataframe[["NOME/RAZÃO SOCIAL","E-MAIL"]]


# In[10]:


emails.info()


# In[24]:


emails.fillna(value = 0, inplace = True)


# In[25]:


emails.head(10)


# In[29]:


counter = 0
for i in emails["E-MAIL"]:
    if i == 0:
        counter+= 1
        
counter
    


# In[59]:


emails_0_copy = emails.loc[emails['E-MAIL'] == 0]
emails_0_copy1 = emails_0_copy[:50].copy()
dfi.export(emails_0_copy1, 'Emails.jpg', max_rows = 50)
emails_0_copy2 = emails_0_copy[51:100].copy()
dfi.export(emails_0_copy2, 'Emails2.jpg', max_rows = 50)
emails_0_copy3 = emails_0_copy[101:].copy()
dfi.export(emails_0_copy3, 'Emails3.jpg', max_rows = 50)


# In[ ]:





# In[ ]:





# In[ ]:




