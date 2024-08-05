#!/usr/bin/env python
# coding: utf-8

# # List Data Structure 

# In[25]:


# COUNT : is used to show how many time a number or and integer is repeated in a list

integer = [11, 12 ,23, 34 ,34, 12,24, 10, 1, 34, 2 ,4 ,6]
string = ['Pakistan', 'India', 'Afghistan', 'Bangladesh', 'Iran', 'Nepal']
x = integer.count(34)
x
y = string.count('India')
y
print(x,"   ",  y)


# In[26]:


# APPEND : us to add element at the last of list 

integer.append(80)
string.append('Australia')

print(integer, "    ", string)
print()

# we can also append to list together

integer.append(string)
print(integer)


# In[27]:


# POP : use to removes an item at the specified index from the list.

a = integer.pop(-1)
b = string.pop(2)

print(integer ,"   ",string )
print()
print(a,"                        ",b)


# In[28]:


# Del : The del statement can be used to delete an entire list or specific item from the list

del(integer[3])
del(string[3])

print(integer, '   ' ,string )


# In[29]:


# Remove : to remove any item from the list directly put the value of the item 

integer.remove(12)
string.remove('India')

print(integer, "   ", string)


# In[30]:


# Insert : we can insert any item at any postiion while the previous item moves to the right

integer.insert(5, 25)
string.insert(2, 'America')

print(integer, '      ', string)


# In[31]:


# Miximum : maximum value
max(integer), min(integer)


# In[32]:


# Sorting : arrange in a sequence 

integer.sort()
print(integer)

# Rreverse sort

integer.reverse()
integer


# In[33]:


string.sort()
print(string)

string.reverse()
string


# In[38]:


# # extend : combine or concatnate two list together
x = [1, 2, 3, 4, 5]
y = ['red', 'green', 'yellow']

x.extend(y)

print(x)


# In[47]:


# Index : get intex number of the specific value from the lsit

x.index(2), y.index('red')


# # List Iteration

# In[63]:


a = [1, 3, 5, 6, 7, 9 ,10]
t=  len(a)

for n in range(t-1, -1, -1):
    print(a[n])


# In[70]:


# 2nd method 

for n in (a):
    print(n)


# In[75]:


x = ['appel', 'orange', 'banana', 'pineapple']
s = len(x)

for n in range(s):
    print(x[n])


# In[76]:


for b in (x):
    print(b)


# # List Comprehension

# In[93]:


a = ['stars']
for l in range(1, 20, 2):
    a.append(l)
print(a)


# In[88]:


n = [c for c in range(1, 50)]
print(n)


# In[135]:


# zip function : is used to iterate two lists at same time

l = [1, 2, 4, 5, 6, 7]
l1 = ['cow', 'ox', 'tiger', 'lion', 'monkey', 'fox']

for a, b in zip(l, l1):
    print(a, b)


# In[138]:


# 2nd method
a = len(l)
for n in range(a):
    print(l[n], l1[n])


# In[156]:


# convert string to list
b = input('Enter the value ')
l =b.split();
print(l)


# In[ ]:


a = []
for n in range(4):
    c =  input('Enter the value'+str(a)+':-')
    a.append(n)
print(l)


# # Tuple Data Structure

# In[104]:


a = (12, 23, 34, 23, 34, 1, 3, 5, 6)
print(a, type(a))


# In[115]:


min(a), max(a),'   ', sorted(a),'    ', sum(a),'    ' a.index(12)


# In[131]:


tup = ('banana', 2,'cherry', 'mango', 5, 6)
a = len(tup)

for n in range(a):
    print(tup[n])


# # Set Data Structure

# In[2]:


st = {1, 2, 3 , 4, 5, 6}
print(st, type(st))


# In[6]:


# Add
st.add(20)
st


# In[12]:


# Remove 
st.remove(20)
st


# In[16]:


# Discard
st.discard(3)
st


# In[18]:


# Union

a = {1, 2, 3, 4, 5, 6}
b = {2, 4, 6, 8, 10, 12}

a.union(b)


# In[19]:


# Intersection

x = {1, 2, 3, 4, 5, 6}
y = {2, 4, 6, 8, 10, 12}

a.intersection(b)


# # Dictionary Data Type

# In[36]:


# unorder data type
# key and values
# {}

d={
    
    'Name' : 'Ehtijad', 
    'Class' : 12,
    'Age' : 18  
}

print(d, type(d))


# In[37]:


print(d["Class"])


# In[38]:


a = d["Age"]
print(a)


# In[39]:


b = d["Name"]
b


# In[40]:


for i in d:
    print(i)


# In[41]:


for n in d:
    print(d[n])


# In[42]:


# FUNCTION
# GET
d={
    'Name' : 'Ehtijad', 
    'Class' : 12,
    'Age' : 18  
}
r = d.get("Name"), d.get('Age')
print(r)


# In[43]:


g=d.get("Class")
print(g)


# In[44]:


# keys
d={
     'Name' : 'Ehtijad', 
    'Class' : 12,
    'Age' : 18  
}
a= d.keys()
a


# In[45]:


for n in d.keys():
    print(n)


# In[46]:


# values
d={
    'Name' : 'Ehtijad', 
    'Class' : 12,
    'Age' : 18  
}
for k in d.values():
    print(k)


# In[47]:


# items: work on two parameters
# 
print('Keys      Values')
print()
d={
    'Name' : 'Ehtijad', 
    'Class' : 12,
    'Age' : 18 
}
for a, b in d.items():
     print(a,'    ',b)


# In[48]:


# del
d={
    'Name' : 'Ehtijad', 
    'Class' : 12,
    'Age' : 18
}
del d["Age"]
print(d)


# In[49]:


d['Class'] = '10'
d


# In[50]:


#pop
d.pop('Class')
print(d)


# In[51]:


# dict():keys become keys and value become value

name = 'Ehtijad'
age = 20
d = {'Name': name, 'age': age}
print(d)


# In[52]:


#update
d={
     'Name' : 'Ehtijad', 
    'Class' : 12,
    'Age' : 18
}
d.update({"Age" : "18years"})
print(d)


# In[53]:


#dict()

d = {'name': 'ehtijad', 'age': 20}
print(d)


# In[54]:


# PYTHON NESTED DICTIONARY

school={
    'Kings':{"Students":2500, 'Boys' : 1500 , 'Girls' : 1000},
    
    "Public":{"Students":10000,'Boys' : 6500 , 'Girls' : 3500},
    
    "APSAC":{"Students":5000,'Boys' : 2500 , 'Girls' : 2500},
}
print(school, type(school))


# In[55]:


school.get('Kings')


# In[56]:


school.get('APSAC')


# In[57]:


school['Kings']['Boys']


# In[58]:


school['APSAC']['Girls']


# In[59]:


for Keys, Values in school.items():
    print(Keys, Values)


# In[60]:


print('School   Boys    Girls')
for Keys, Values in school.items():
    print(Keys,'  ', Values['Boys'],'   ',  Values['Girls'])


# In[61]:


school['Public']['Girls'] = 4000
school

