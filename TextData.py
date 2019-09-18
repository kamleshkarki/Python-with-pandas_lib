#!/usr/bin/env python
# coding: utf-8

# In[21]:


import nltk
import sklearn
print('The nltk version is {}.'.format(nltk.__version__))
print('The scikit-learn version is {}.'.format(sklearn.__version__))


# In[32]:


import numpy as np
import pandas as pd 
import os


# In[83]:


Location= pd.read_csv('C:/Users/ayn-pc2/Desktop/T/update.csv')
Location.head()
print(Location)


# In[69]:


from nltk.tokenize import word_tokenize
with open ('C:/Users/ayn-pc2/Desktop/T/update.csv') as fin:
    tokens = word_tokenize(fin.read())


# In[88]:


Location= pd.read_csv('C:/Users/ayn-pc2/Desktop/T/update.csv')
Location.head()


# In[24]:


#Location["update.csv"][0]


# In[87]:


Location["glusr_usr_company_desc"]


# In[49]:


Location["glusr_usr_company_desc"][0]


# In[24]:


#this is for hold multiline row**
Location["glusr_usr_company_desc"][[0,1,2,3,4,5]]


# In[89]:


import nltk


# In[91]:


#nltk.word_tokenize(Location["glusr_usr_company_desc"])


# In[53]:


nltk.word_tokenize(Location["glusr_usr_company_desc"][0])


# In[61]:


nltk.word_tokenize(Location["glusr_usr_company_desc"][1])


# In[35]:


Location["glusr_usr_company_desc"][0]


# In[20]:


nltk.tokenize.WhitespaceTokenizer().tokenize(Location["glusr_usr_company_desc"][0])


# In[38]:


nltk.tokenize.WordPunctTokenizer().tokenize(Location["glusr_usr_company_desc"][0])


# In[56]:


nltk.tokenize.TreebankWordTokenizer().tokenize(Location["glusr_usr_company_desc"][0])


# In[41]:


Location["glusr_usr_company_desc"][0]


# In[42]:


#STEMMING
words  = nltk.tokenize.WhitespaceTokenizer().tokenize(Location["glusr_usr_company_desc"][0])


# In[43]:


df = pd.DataFrame()
df['OriginalWords'] = pd.Series(words)


# In[44]:


#porter's stemmer
porterStemmedWords = [nltk.stem.PorterStemmer().stem(word) for word in words]
df['PorterStemmedWords'] = pd.Series(porterStemmedWords)


# In[45]:


#SnowBall stemmer
snowballStemmedWords = [nltk.stem.SnowballStemmer("english").stem(word) for word in words]


# In[46]:


df['SnowballStemmedWords'] = pd.Series(snowballStemmedWords)
df


# In[48]:


#LEMMATIZATION
words  = nltk.tokenize.WhitespaceTokenizer().tokenize(Location["glusr_usr_company_desc"][0])


# In[49]:


df = pd.DataFrame()
df['OriginalWords'] = pd.Series(words)


# In[52]:


#WordNet Lemmatization
wordNetLemmatizedWords = [nltk.stem.WordNetLemmatizer().lemmatize(word) for word in words]
df['WordNetLemmatizer'] = pd.Series(wordNetLemmatizedWords)
df


# In[ ]:





# In[ ]:




