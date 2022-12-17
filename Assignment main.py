#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a program to get the Fibonacci series between 0 to 50.
start = int(input("enter the start num:"))
end = int(input("enter the end num:"))
x,y = 0,1
while y<end:
    print(y)
    x,y = y,x+y


# In[2]:


#Write a python program that accepts a word from the user and reverse it.
x = input("enter the word to reverse:")
for i in range(len(x)-1,-1,-1):
    print (x[i],end=" ")


# In[4]:


#Write a Python program to count the number of even and odd numbers from a series of numbers(1,2,3,4,5,6,7,8,9).
x = eval(input("enter the series:"))
even_count, odd_count = 0, 0
for i in x:
    if i%2==0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even numbers:",even_count)
print("Number of odd numbers:",odd_count)


# In[ ]:




