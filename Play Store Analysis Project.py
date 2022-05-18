#!/usr/bin/env python
# coding: utf-8

# # Importing Necessary Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action="ignore",category=FutureWarning)


# # Importing the data

# In[2]:


df=pd.read_csv("C:\\Users\\Dell\\Desktop\\PG in Data Analysis EDU Bridge\\Python\\playstore-analysis.csv")


# In[3]:


#display the first 5 rows from the dataset
df.head()


# In[4]:


#display the last 5 rows from the dataset
df.tail()


# In[5]:


#checking the datatypes of the columns
df.dtypes


# In[6]:


#getting the information about our dataset,ie total number of rows ,total number of columns,
#how much nonnull values present and their data types
df.info()


# In[54]:


df.shape


# In[7]:


df.describe()


# In[8]:


#Find the shape of our dataset
df.shape


# # Data Cleaning

# In[9]:


#checking the null values
df.isnull().sum()


# In[10]:


#checking total number of null values present in the data
df.isnull().sum().sum()


# In[11]:


#checking the outlier using boxplot
df.boxplot("Rating")


# In[12]:


df.hist("Rating")
plt.show()


# In[13]:


sns.distplot(df.Rating)
plt.show()


# In[14]:


#cheking the rating <1 present in the data or not
df[df.Rating<1]


# In[15]:


#cheking the rating >5 present in the data or not
df[df.Rating>5]


# In[16]:


#we find there is one row present in the data that are more than 5 ratings ,so we use drop function for dropping the data 
#as it is an outlier
df.drop([10472],inplace=True)


# In[17]:


#to check the index no [10472] drop from the data or not
df[10470:10475]


# In[18]:


#after droping the rating> 5 we use boxplot to check the outlier
sns.boxplot(df.Rating)
plt.show()


# In[19]:


#replace the null values with median in Rating column
x=df["Rating"].median()
df["Rating"].fillna(x,inplace=True)


# In[20]:


#Replace the null values with mode in Content Rating column
z=df["Content Rating"].mode()[0]
df["Content Rating"].fillna(z,inplace=True)

#Replace the null values with mode in Current Ver column
C=df["Current Ver"].mode()[0]
df["Current Ver"].fillna(C,inplace=True)

#Replace the null values with mode in Android Ver column
A=df["Android Ver"].mode()[0]
df["Android Ver"].fillna(A,inplace=True)

#Replace the null values with mode in Type column
T=df["Type"].mode()[0]
df["Type"].fillna(T,inplace=True)


# In[21]:


#after replacing all the null values we use heat map to vishualize is there any null values present in the data
plt.figure(figsize=(5,5))
sns.heatmap(df.isnull())
plt.show()


# In[22]:


df.isnull().sum()


# In[23]:


#Removing the strings("$","+,",") present in the price,intsalls and also change the
#data type object to float and int
df["Price"]=df["Price"].apply((lambda x:str(x).replace("$"," ")if "$" in str(x) else str(x)))
df["Price"]=df["Price"].apply(lambda x:float(x))
df["Reviews"]=pd.to_numeric(df["Reviews"],errors="coerce")


# In[24]:


df["Installs"]=df["Installs"].apply(lambda x:str(x).replace("+","")if "+" in str(x) else str(x))
df["Installs"]=df["Installs"].apply(lambda x:str(x).replace(",","")if "," in str(x) else str(x))
df["Installs"]=df["Installs"].apply(lambda x:float(x))


# In[25]:


df.dtypes


# In[26]:


df.describe()


# # Data Analysing  & Visualising 

# In[27]:


df.columns


# In[28]:


#to find the Average App Rating
x=df["Rating"].mean()


# In[29]:


x


# In[30]:


sns.countplot([x])


# In[31]:


plt.figure(figsize=(15,9))
plt.xlabel("Rating")
plt.ylabel("Frequency")
ax=plt.axes()
ax.set(facecolor="grey")
graph = sns.kdeplot(df.Rating, color="Blue", shade = True)
plt.title('Distribution of Rating',size = 20);


# In[32]:


#find the total number of unique category
df['Category'].nunique()


# In[33]:


#to finding which category getting the highest average rating
y=df.groupby('Category')['Rating'].mean().sort_values(ascending=False)


# In[34]:


y


# In[35]:


plt.figure(figsize=(10,7))
plt.plot(y,color="g",marker='o',markerfacecolor="b")
ax=plt.axes()
ax.set(facecolor="yellow")
plt.xticks(rotation="vertical")
plt.show()


# In[36]:


plt.figure(figsize=(15,7))
Category=df["Category"]
Rating=df["Rating"]
sns.barplot(Category,Rating,palette="rocket")
ax=plt.axes()
ax.set(facecolor="grey")
plt.xticks(rotation="vertical")
plt.show()


# In[37]:


#to check Top categories on play store
plt.figure(figsize=(12,12))
most_cat = df.Category.value_counts()
sns.barplot(x=most_cat, y=most_cat.index, data=df)


# In[38]:


#Android ver in category
Type_cat = df.groupby('Category')['Android Ver'].value_counts().unstack().plot.barh(figsize=(8,15), width=1)
plt.show()


# In[39]:


#to find the total number of Apps having 5 star Rating
len(df[df['Rating']==5.0])


# In[40]:


#finding average values of Reviews
df["Reviews"].mean()


# In[41]:


#find the total number of free apps and paid apps
df["Type"].value_counts()


# In[42]:


plt.figure(figsize=(10,10))
labels = df['Type'].value_counts(sort = True).index
sizes = df['Type'].value_counts(sort = True)
colors = ["blue","lightgreen"]
explode = (0.2,0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)
plt.title('Percent of Free Vs Paid Apps in store',size = 20)
plt.show()


# In[43]:


#find the highest rating in which types free or paid Apps.
sns.barplot(df.Type,df.Rating)
plt.show()


# In[44]:


sns.lineplot(df.Type,df.Rating)


# In[45]:


#finding which Apps have maximum Reviews
df[df["Reviews"].max()==df["Reviews"]]["App"]


# In[46]:


#Display top 5 Apps having highest Reviews
index=df["Reviews"].sort_values(ascending=False).head().index


# In[47]:


df.iloc[index]["App"]


# In[48]:


#Display top 5 Apps having highest Installs
index=df["Installs"].sort_values(ascending=False).head(6).index


# In[49]:


z=df.iloc[index]["App"]
z


# In[50]:


plt.figure(figsize=(10,7))
ax=plt.axes()
ax.set(facecolor="grey")
sns.barplot(x=z,y=df.Installs,palette="rocket")
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("Apps",fontsize=15)
plt.ylabel("Installs",fontsize=15)
plt.title("Top 5 Apps having highest Installs")
plt.show()


# In[51]:


#cheking which category has highest paid apps
plt.figure(figsize=(15,7))
plt.plot(df.Price,df.Category,color="y",marker='o',markerfacecolor="b")
plt.title("Category vs Price")
plt.xlabel("Price",fontsize=15)
plt.ylabel("Category",fontsize=15)
ax=plt.axes()
ax.set(facecolor="black")
plt.show()


# In[52]:


#cheking while rating increaes price is also increasing
plt.figure(figsize=(7,7))
plt.scatter(df.Rating,df.Price,color="r")
plt.title("Rating vs Price")
plt.xlabel("Rating",fontsize=15)
plt.ylabel("Price",fontsize=15)
ax=plt.axes()
ax.set(facecolor="purple")
plt.show()


# # Conclusion

# In[ ]:


Following are the conclusion of the  above Play Store Analysis
1.we can come to the conclusion that most of the apps in the google play store are rated between 3.5 to 4.8.
2.we can see that 92%(Approx.) of apps in the google play store are free and 8%(Approx.) are paid
3.Here in our dataset there are total of 33 categories in the dataset  
4.we can see that the play store most of the apps are under Family & Game Category and least are of Beauty & Comics Category
5.Events and Education category are getting the highest rating

