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

ax2 = plt.subplot(2,2,3)
ax2 = sns.regplot(x='User Rating', y='Box office (USD)', data=revenue, x_jitter=.1,color='g',marker='+')
#ax2.text(6800,1.1e9,'r=0.78',fontsize=15)
plt.title('Box office by User Rating',fontsize=15)
plt.xlabel('Critic Numbers',fontsize=13)
plt.ylabel('Box office',fontsize=13)

ax2 = plt.subplot(2,2,4)
ax2 = sns.regplot(x='User Numbers', y='Box office (USD)', data=revenue, x_jitter=.1,color='g',marker='+')
#ax2.text(6800,1.1e9,'r=0.78',fontsize=15)
plt.title('Box office by User Numbers',fontsize=15)
plt.xlabel('User Critic Numbers',fontsize=13)
plt.ylabel('Box office',fontsize=13)


# In[77]:


sns.heatmap(data_corr,annot=True) 


# # Number of Movie Genre

# In[147]:


import pandas as pd
data = pd.read_csv('2017_movie_dataframe.csv')
data.head()


# In[148]:


# create all genre set
import re
movie_genre = data['Genre']
genre = set()   
genre_set = set()
for item in movie_genre:
    genre.update(item.strip().split(','))
for item in genre:
    genre_set.add(item.strip())
genre_set


# In[150]:


genre_df = pd.DataFrame()
for genre in genre_set:
    genre_df[genre] = data['Genre'].str.contains(genre).map(lambda x: 1 if x else 0)
genre_sum = genre_df.sum().sort_values(ascending = False)
fig = plt.figure(figsize = (8,8))
ax = plt.subplot(1,1,1)
ax = genre_sum.plot.bar()
plt.xticks(rotation=60)
plt.title('Film genre in 2017',fontsize = 18)
plt.xlabel('genre', fontsize = 18)
plt.ylabel('count', fontsize =18)


# # Revenue of Movie Genre

# In[162]:


profit_by_genre = pd.Series(index = genre_set)
genre_df['Box_office'] = data['Box office (USD)']
genre_df = genre_df[genre_df['Box_office'] != '-']
genre_df['Box_office'] = genre_df['Box_office'].apply(pd.to_numeric)
for genre in genre_set:
    profit_by_genre.loc[genre] = genre_df[genre_df[genre] == 1]['Box_office'].sum()


# In[ ]:


dhdjfiebcvhdgds


# In[ ]:


hjshfoiregi3

