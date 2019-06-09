#!/usr/bin/env python
# coding: utf-8

# In[125]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[126]:


page=requests.get("http://scores.sify.com")
page


# In[127]:


#page.content


# In[128]:


soup=BeautifulSoup(page.content,'html.parser')


# In[129]:


print(soup.prettify())


# In[130]:


url=[]
for i in soup.find_all('div',class_="scoresbox-center"):
    try:
        url.append(i.h2.a.get('href'))
    except:
        break
print(url)


# In[158]:


for i in matches:
    url=requests.get(i)
    #print(i)
    soup=BeautifulSoup(url.text,'html.parser')
    info=soup.find('div',class_='team-live')
    for a in info:
        print(a.get_text())
    print("\n")
    table_body=soup.find('tbody')
    links=table_body.find_all('a')
    Batsman=[]
    for k in links:
        Batsman.append(k.get_text())
    rows = table_body.find_all('tr')
    R=[]
    B=[]
    F=[]
    S=[]
    for row in rows[0:-2]:
        cols=row.find_all('td')
        cols=[x.get_text() for x in cols]
        R.append(cols[2])
        B.append(cols[3])
        F.append(cols[4])
        S.append(cols[5])
    ScoreBoard=pd.DataFrame({
    "Batsman":Batsman,
    "Runs":R,
    "Balls":B,
    "4s":F,
    "6s":S
    })
    print(ScoreBoard)
    print("\n")
    table_body1=soup.find_all('tbody')[3]
    links=table_body1.find_all('a')
    Batsman=[]
    for k in links:
        Batsman.append(k.get_text())
    rows = table_body.find_all('tr')
    R=[]
    B=[]
    F=[]
    S=[]
    for row in rows[0:-2]:
        cols=row.find_all('td')
        cols=[x.get_text() for x in cols]
        R.append(cols[2])
        B.append(cols[3])
        F.append(cols[4])
        S.append(cols[5])
    R=[]
    B=[]
    F=[]
    S=[]
    for row in rows[0:-2]:
        cols=row.find_all('td')
        cols=[x.get_text() for x in cols]
        R.append(cols[2])
        B.append(cols[3])
        F.append(cols[4])
        S.append(cols[5])
    try:
        ScoreBoard=pd.DataFrame({
            "Batsman":Batsman,
            "Runs":R,
            "Balls":B,
            "4s":F,
            "6s":S
        })
        print(ScoreBoard)
        print("\n")
        print("------------------------------------------------------------------------------------------------")
        print("\n")
    except:
        pass


# In[ ]:


url


# In[30]:


for i in ssA.find_all('tbody'):
            print(i.text)
            print("\n")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import pandas as pd 
ScoreBoardAUS=pd.DataFrame({
    "Batsman":Batsman,
    "Runs":R,
    "Balls":B,
    "4s":Fours,
    "6s":Sixes
})
ScoreBoardAUS


# In[ ]:





# In[23]:


table_body=soup.find_all('tbody')
WI=table_body[3]


# In[24]:


rows1=WI.find_all('tr')
for row in rows1[0:-2]:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    print(cols)


# In[25]:


R=[]
for row in rows1[0:-2]:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    R.append(cols[2])


# In[26]:


B=[]
for row in rows[0:-2]:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    B.append(cols[3])


# In[27]:


Fours=[]
for row in rows[0:-2]:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    Fours.append(cols[3])


# In[28]:


Sixes=[]
for row in rows[0:-2]:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    Sixes.append(cols[4])


# In[29]:


ssW=soup.find_all('div',class_='col-md-6')
my_table2=ssW.find_all(class_='table table-hover batting')
my_table2


# In[ ]:


import pandas as pd 
ScoreBoardWI=pd.DataFrame({
    "Batsman":Batsman,
    "Runs":R,
    "Balls":B,
    "4s":Fours,
    "6s":Sixes
})
ScoreBoardWI

