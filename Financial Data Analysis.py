#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


sns.set_theme(style="whitegrid")


# In[3]:


df = pd.read_csv("C:\\Users\\Amrutha\\Downloads\\transactions.csv")


# In[4]:


df['amount'] = df['amount'].replace('[\$,]', '', regex=True).astype(float)


# In[5]:


df['date'] = pd.to_datetime(df['date'], errors='coerce')


# In[6]:


df['Year'] = df['date'].dt.year
df['Month'] = df['date'].dt.month_name()
df['Hour'] = df['date'].dt.hour


# In[7]:


print("Dataset Shape:", df.shape)
print("Columns:", df.columns)
print(df.head())


# In[8]:


total_transactions = len(df)
total_amount = df['amount'].sum()
avg_transaction = df['amount'].mean()


# In[9]:


print("\n📊 Transaction Summary:")
print(f"• Total transactions: {total_transactions:,}")
print(f"• Total transaction value: ${total_amount:,.2f}")
print(f"• Average transaction value: ${avg_transaction:,.2f}")


# In[10]:


top_states = df['merchant_state'].value_counts().nlargest(10)


# In[11]:


plt.figure(figsize=(10,5))
sns.barplot(x=top_states.index, y=top_states.values, palette="viridis")
plt.title("Top 10 Merchant States by Transaction Count")
plt.xlabel("Merchant State")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.show()


# In[12]:


avg_amount_state = df.groupby('merchant_state')['amount'].mean().nlargest(10)


# In[13]:


plt.figure(figsize=(10,5))
sns.barplot(x=avg_amount_state.index, y=avg_amount_state.values, palette="coolwarm")
plt.title("Top 10 States by Average Transaction Amount")
plt.xlabel("Merchant State")
plt.ylabel("Average Transaction ($)")
plt.xticks(rotation=45)
plt.show()


# In[14]:


monthly_volume = df.groupby('Month')['amount'].sum()
order = ["January","February","March","April","May","June","July","August","September","October","November","December"]


# In[15]:


plt.figure(figsize=(12,6))
sns.barplot(x=monthly_volume.index, y=monthly_volume.values, order=order, palette="magma")
plt.title("Total Transaction Value by Month")
plt.xlabel("Month")
plt.ylabel("Total Amount ($)")
plt.xticks(rotation=45)
plt.show()


# In[16]:


hourly_avg = df.groupby('Hour')['amount'].mean()


# In[17]:


plt.figure(figsize=(10,5))
sns.lineplot(x=hourly_avg.index, y=hourly_avg.values, marker='o', color='teal')
plt.title("Average Transaction Value by Hour of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Average Amount ($)")
plt.show()


# In[18]:


most_active_state = df['merchant_state'].value_counts().idxmax()
highest_spend_state = df.groupby('merchant_state')['amount'].sum().idxmax()

print("\n💡 Insights:")
print(f"• Most active merchant state (by count): {most_active_state}")
print(f"• State with highest total spending: {highest_spend_state}")
print(f"• Average transaction value across dataset: ${avg_transaction:,.2f}")


# In[ ]:





# In[ ]:




