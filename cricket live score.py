#!/usr/bin/env python
# coding: utf-8

# In[37]:


from bs4 import BeautifulSoup
import requests


# In[38]:


source= requests.get('http://www.espncricinfo.com/scores').text


# In[39]:


soup=BeautifulSoup(source,'html.parser')


# In[40]:


print(soup.prettify())


# In[55]:


for j in soup.find_all("div",{'class':"scoreCollection cricket"}):
    for i in j.find_all("div",{'class':"cscore_overview"}):
        a = i.text
        print(a)


# In[ ]:





# In[ ]:




