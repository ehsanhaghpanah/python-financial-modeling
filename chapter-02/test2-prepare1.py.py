#!/usr/bin/env python
# coding: utf-8

# محاسبه بتا و ضریب تغییرات وبازده روزانه شاخص و سهم خساپا:
# 
# 

# In[1]:


import pandas as pd
import numpy as np
import tsemodule5 as tm5


# In[2]:


Shakheskol=pd.read_csv('C:/Users/Ateeq/Downloads/shakhes_1.csv', parse_dates=['dateissue'])
Shakheskol=Shakheskol[['dateissue','Value']]


# In[3]:


Shakhes=Shakheskol[:10]


# In[4]:


khesapa=tm5.stock("خساپا",standard=True)
KHESAPA=khesapa[:10]


# In[5]:


KHESAPA['daily_return'] =KHESAPA['Close'].pct_change(1)
Shakhes['daily_return'] =Shakhes['Value'].pct_change(1)


# In[6]:


display(Shakhes,KHESAPA)


# In[7]:


KHESAPA_CV = KHESAPA['daily_return'].std()/KHESAPA['daily_return'].mean()
print('KHESAPA CV:\n',KHESAPA_CV,sep='')


# In[8]:


Shakhes_CV = Shakhes['daily_return'].std()/Shakhes['daily_return'].mean()
print('Shakhes CV:\n',Shakhes_CV,sep='')


# In[9]:


stock = pd.DataFrame(np.concatenate([Shakhes['daily_return'].dropna().values.reshape(-1,1),KHESAPA['daily_return'].dropna().values.reshape(-1,1)],axis=1))
stock.columns = ['Shakhes','KHESAPA']
Covariance=stock.cov()
variance=KHESAPA['daily_return'].var()
display(Covariance , variance)


# In[10]:


Beta=Covariance/variance
Beta


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




