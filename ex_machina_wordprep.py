#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import nltk
import sys
from nltk.corpus import stopwords


# In[2]:


data_train = pd.read_csv('data_train.csv', encoding='latin-1')


# In[3]:


stop_words = set(stopwords.words('english')) 


# In[4]:


rejected_sw = ["aren't", "couldn", "couldn't", "didn", "didn't", "doesn", "doesn't", "don't", "hadn", "hadn't", "hasn", "hasn't", "haven't", "isn", "isn't", "mightn", "mightn't", "mustn", "mustn't", "needn", "needn't", "no", "nor", "not", "shan't", "shouldn", "shouldn't", "wasn", "wasn't", "weren't", "won't", "wouldn", "wouldn't",  ]


# In[5]:


acc_stopwords = []
for i, value in enumerate(stop_words):
    if value not in rejected_sw:
        acc_stopwords.append(value)


# In[6]:


filtered_sentences = []
for i,words in enumerate(data_train['reviews.text']):
    print (i)
    filtered = [word for word in words.split() if word not in acc_stopwords]
    filtered_sentences.append(' '.join(filtered))


# In[7]:


data_train['filtered_reviews'] = pd.Series(filtered_sentences, index=data_train.index)
data_train


# In[8]:


data_train.to_csv('stem_train.csv', index=False)


# In[9]:


data_test = pd.read_csv('data_test.csv',  encoding='latin-1')


# In[10]:


filtered_sentences_test = []
for i,words in enumerate(data_test['reviews.text']):
    print (i)
    filtered = [word for word in words.split() if word not in acc_stopwords]
    filtered_sentences_test.append(' '.join(filtered))


# In[11]:


data_test['filtered_reviews'] = pd.Series(filtered_sentences_test, index=data_test.index)
data_test


# In[12]:


data_test.to_csv('stem_test.csv', index=False)


# In[ ]:




