#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
print(pd.__version__)
import numpy as np
print(np.__version__)
import matplotlib as plt
print(matplotlib.__version__)


# In[6]:


csv_path = 'bdd_universal_test.csv'

df = pd.read_csv(csv_path, delimiter=';')

print(df.head())


# In[7]:


df.info()


# In[8]:


# je vais commencer par convertir en numérique et remplacer les erreurs par NaN
df['Var_Pct'] = pd.to_numeric(df['Var_Pct'], errors='coerce')


# In[9]:


# Même chose pour la colonne année
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')


# In[11]:


#Conversion de la colonne au format Date
df['Date_from'] = pd.to_datetime(df['Date_from'], errors='coerce', dayfirst=True)


# In[12]:


#Je vérirfie les NULL
print(df.isnull().sum())


# In[14]:


#je supprime les valeurs Null
df = df.dropna(subset=['Var_Pct'])
df = df.dropna(subset=['Year'])


# In[15]:


print(df.isnull().sum())


# In[16]:


#je lance une analyses pour observer certaines stats
print(df.describe())


# In[ ]:





# In[22]:


#Observation de la répartition des distribiteurs par nombre de titre afin d'avoir une visualisation quantitative
plt.figure(figsize=(12, 6))
sns.countplot(y='Distributeur', data=df, order=df['Distributeur'].value_counts().index)
plt.title('Répartition des Distributeurs')
plt.xlabel('Nombre de Titres')
plt.ylabel('Distributeur')
plt.show()


# In[25]:


#Distribution des Streams : je visualise la distribution des Streams pour détecter les éventuelles anomalies (valeurs abhérantes) ou voir certaines tendances
plt.figure(figsize=(10, 6))

plt.hist(df['Streams'], bins=30, edgecolor='k', alpha=0.7)
plt.title('Distribution des Streams')
plt.xlabel('Nombre de Streams')
plt.ylabel('Fréquence')
plt.show()


# In[ ]:




