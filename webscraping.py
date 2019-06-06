#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup as bs


# In[54]:


page=requests.get('http://scores.sify.com/live-cricket-scores/ICC-Cricket-World-Cup-2019/SOUTH-AFRICA_vs_INDIA_JUN05_2019.shtml')
#page.content


# In[48]:


soup=bs(page.content,'html.parser')


# In[55]:


#soup.find_all(class_='clearfix')


# In[76]:


tab=soup.find('table')


# In[68]:


table=soup.find_all('td')


# In[72]:


table


# In[81]:


body=list(tab.children)[1]


# In[82]:


body


# In[85]:


body.get_text()


# In[ ]:




