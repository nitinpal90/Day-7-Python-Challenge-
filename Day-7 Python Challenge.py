#!/usr/bin/env python
# coding: utf-8

# # Day-7 Python Challenge

# # Create a Single line String 

# In[1]:


a = 'Python'
print(a)


# # Create a Double Line String

# In[2]:


b = "Py"
print(b)
print(type(b))


# # Create a Multiline String

# In[8]:


a = """INDIA ARE T20 WORLD CHAMPIONS AFTER 17 YEARS! It's been a long, 
long wait for India and they now join West Indies and England as 
the only three teams to have won the Men's T20 World Cup two times. 
You really couldn't ask for more, what a grand finale 
we have had here in Barbados and both sides gave it their all!  """
print(a)


# In[9]:


print(len(a))


# # Indexing of String

# In[4]:


a = "Ravan"
print(a[3])


# In[5]:


a = "Ravan"
print(a[-3])


# # Slicing of String

# In[6]:


s = "Hello Foks"
print(s[0:4])


# # Length of the String

# In[10]:


a = "Student" ## Number of character in string
print(len(a))


# # Upper Method 

# In[11]:


a = "students are not crying"
print(a.upper())


# # Lower Method

# In[12]:


b = "STUDENTS ARE CRYING"
print(b.lower())


# # Replace Function

# In[13]:


a = "Your a Good Boy"
print(a.replace("Good", "Bad"))


# # Find Function

# In[15]:


a = "Python is King"
b = a.find("i")
print(b)

