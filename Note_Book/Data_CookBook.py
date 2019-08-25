#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd


# In[10]:


print('hello')


# In[28]:


#Location= pd.read_excel('c:/users/RamaKrishna/Desktop/Data/Datarecord.xlsx')
#Location df= pd.DataFrame(XYZ_web)


# In[49]:


data= {
    #'customer':[Cus1,Cust2,Cust3,Cust4],
    'apple' :[3,4,2,3],
    'orange': [4,8,7,8],
    'Grapes' :[5,8,10,7]
}


# In[50]:


df = pd.DataFrame(data)


# In[51]:


purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])


# In[52]:


df = pd.DataFrame(data, index=['Kamlesh','Amit','Lauli','David'])


# In[53]:


print(df)


# In[40]:


XYZ_web= {'Day':[1,2,3,4,5,6], "Visitors":[1000, 700,6000,1000,400,350], "Bounce_Rate":[20,20, 23,15,10,34]}


# In[41]:


df= pd.DataFrame(XYZ_web)


# In[42]:


print(df)


# In[ ]:




