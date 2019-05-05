#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt


# In[5]:


data = pd.read_csv("xAPI-Edu-Data (1).csv")
data.head(10)


# In[306]:


data.describe()


# In[307]:


data.info()


# In[6]:


#raised hand and visisted source seems more correlate to the grade

melt= pd.melt(data,id_vars='Class',value_vars=['raisedhands','VisITedResources','AnnouncementsView','Discussion'])
print(melt)
g=sns.swarmplot(x='variable',y='value',hue='Class' , data=melt,palette={'H':'lime','M':'Black','L':'Blue'})
plt.ylabel('Values from zero to 100')
plt.title('High, middle and low level students')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('Class participation and distribution of grades')
for item in g.get_xticklabels():
    item.set_rotation(60)


# In[294]:


data.corr()


# In[6]:


#it seems that there is strong correlation between raisedhands and vistTedResource
a=sns.pairplot(data,hue='Class',palette="husl")

plt.rcParams['figure.figsize']=(4,5)


# In[21]:


sns.countplot(x='ParentschoolSatisfaction',data = data, hue='Class',palette='bright')
plt.title('Parental satisfaction with the school and distribution of student achievement')
plt.show()


# In[23]:


#mother seems have more impact on student score
data["good"] = data["Class"][(data["Class"] == "H")]

data['good'] = np.where(data['Class']=='H',1,0)

sns.factorplot('Relation','good',data=data)
plt.title('Parental influence on child performance')


# In[ ]:





# In[31]:



plot = sns.swarmplot(x='Class', y='Discussion', hue='gender', order=['L', 'M', 'H'], 
              data=data, palette='coolwarm')
plot.set(xlabel='Class', ylabel='Count', title='Gender comparison on discussion')
plt.rcParams['figure.figsize']=(5,5)
plt.show()


# In[32]:


plot = sns.swarmplot(x='Class', y='raisedhands', hue='gender', order=['L', 'M', 'H'], 
              data=data, palette='coolwarm')
plot.set(xlabel='Class', ylabel='Count', title='Gender comparison on rasing hands')
plt.rcParams['figure.figsize']=(5,5)
plt.show()


# In[35]:


plot = sns.swarmplot(x='Class', y='VisITedResources', hue='gender', order=['L', 'M', 'H'], 
              data=data, palette='coolwarm')
plot.set(xlabel='Class', ylabel='Count', title='Gender comparison on visiting Ted resources')
plt.rcParams['figure.figsize']=(5,5)
plt.show()


# In[36]:


plot = sns.swarmplot(x='Class', y='AnnouncementsView', hue='gender', order=['L', 'M', 'H'], 
              data=data, palette='coolwarm')
plot.set(xlabel='Class', ylabel='Count', title='Gender comparison on visiting AnnouncementsView')
plt.rcParams['figure.figsize']=(5,5)
plt.show()


# In[40]:


sns.countplot(x='Topic',data = data, hue='Class',palette='bright')
plt.rcParams['figure.figsize']=(10,10)
plt.title('Distribution of grades on different topics')
plt.show()


# In[ ]:





# In[41]:


sns.countplot(x='gender',data = data, hue='Class',palette='bright')
plt.title('Distribution of grades on different gender')
plt.show()


# In[86]:






sns.countplot(x='NationalITy',data = data, hue='Class',palette='bright',)
plt.title('Distribution of grades on different nationality')
plt.rcParams['figure.figsize']=(15,5)

plt.show()


# In[91]:


sns.countplot(x='Semester',data = data, hue='Class',palette='bright')
plt.title('Distribution of grades on semester')
plt.rcParams['figure.figsize']=(10,10)
plt.show()


# In[ ]:




