#!/usr/bin/env python
# coding: utf-8

# # Box Office

# In[67]:


import pandas as pd
data = pd.read_csv('2017_movie_dataframe.csv')


# In[68]:


data.head()


# In[70]:


data = data[data['Box office (USD)'] != '-']
data['Box office (USD)'] = data['Box office (USD)'].apply(pd.to_numeric)


# In[73]:


data_corr = data[['Critic Rating','Critic Numbers','User Rating','User Numbers','Box office (USD)']].corr()


# In[72]:


import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
revenue = data[['Critic Rating', 'Critic Numbers', 'User Rating', 'User Numbers', 'Box office (USD)']]
fig = plt.figure(figsize=(10,10))
ax1 = plt.subplot(2,2,1)
ax1 = sns.regplot(x='Critic Rating', y='Box office (USD)', data=revenue, x_jitter=.1)
plt.title('Box office by Critic Rating',fontsize=15)
plt.xlabel('Critic Rating',fontsize=13)
plt.ylabel('Box office',fontsize=13)

ax2 = plt.subplot(2,2,2)
ax2 = sns.regplot(x='Critic Numbers', y='Box office (USD)', data=revenue, x_jitter=.1,color='g',marker='+')
#ax2.text(6800,1.1e9,'r=0.78',fontsize=15)
plt.title('Box office by Critic Numbers',fontsize=15)
plt.xlabel('Critic Numbers',fontsize=13)
plt.ylabel('Box office',fontsize=13)