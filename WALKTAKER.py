#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
import pylab as pb
import pandas as pd


# In[4]:


def average_time_heel(name):
    heel_time = 0
    df1 = pd.read_csv(name)
    for i in range(len(df1)):
        heel_time = heel_time + df1['Time'][i]    
    
    heel_avg = heel_time/len(df1)
    return heel_avg

x = average_time_heel("dataTimeHeel.csv")
df1 = pd.read_csv("dataTimeHeel.csv")

if(len(df1)>50):
    lines = []
    with open("dataTimeHeel.csv",'r') as file:
        r = csv.reader(file)
        for i in r:
            lines.append(i)
            for j in i:
                lines.remove(i)
            
    with open('dataTimeHeel.csv', 'w') as w:
        writer = csv.writer(w)
        writer.writerows(lines)


# In[5]:


def average_time_toe(name):
    toe_time = 0
    df2 = pd.read_csv(name)
    for i in range(len(df2)):
        toe_time = toe_time + df2['Time'][i]    
    
    toe_avg = toe_time/len(df2)
    return toe_avg

y = average_time_toe("dataTimeToe.csv")

df2 = pd.read_csv("dataTimeToe.csv")
if(len(df2)>50):
    lines = []
    with open("dataTimeToe.csv",'r') as file:
        r = csv.reader(file)
        for i in r:
            lines.append(i)
            for j in i:
                lines.remove(i)
            
    with open('dataTimeToe.csv', 'w') as w:
        writer = csv.writer(w)
        writer.writerows(lines)


# In[1]:


def input_avg(x,y):
    with open("averageTime.csv",'w',newline='') as file:
        w = csv.writer(file)
        w.writerow(["Heel","Toe"])
        w.writerow([x,y])


# In[2]:


import warnings
from scipy.stats import linregress

def linregress_heel_toe(df1,df2):
    x1 = pb.linspace(0,len(df1),len(df1))
    x2 = pb.linspace(0,len(df2),len(df2))

    z1 = pb.polyfit(df1['Time'],x1,1)
    p1 = pb.poly1d(z1)
    z2 = pb.polyfit(df2['Time'],y1,1)
    p2 = pb.poly1d(z2)

    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x1,p1(x1))
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x2,p2(x2))


# In[26]:


def func(y,x):
    if(y > x):
        print("ALERT!!! YOU MAY SUFFER FROM KNEE PAIN IN FUTURE. SO TRY TO WALK ON HEELS TOO")


# In[27]:


def func(x,y):
    if(x > y):
        print("ALERT!!! YOU MAY SUFFER FROM AUTISM. SO TRY TO WALK ON TOE TOO")


# In[28]:


def fast_walk(slope1,slope2):
    with open("slopes.csv",'w',newline='') as file:
        w = csv.writer(file)
        w.writerow(["Slope Heel","Slope Toe"])
        w.writerow([slope1,slope2])
    
    df3 = pd.read_csv('slopes.csv')
    for i in range(len(df3)):
        if(df3['Slope Heel'][i]<df3['Slope Heel'][i+1]):
            print("ALERT!!! YOU MAYBE WALKING SLOW. SO TRY TO WALK FAST.")


# In[36]:


def different_pattern(std_err1,std_err2):
    with open("std_err.csv",'w',newline='') as file:
        w = csv.writer(file)
        w.writerow(["Standard Error Heel","Standard Error Toe"])
        w.writerow([std_err1,std_err2])
    
    df4 = pd.read_csv('std_err.csv')
    for i in range(len(df4)):
        if(df4['Standard Error Heel'][i]<df4['Standard Error Toe'][i+1]):
            print("ALERT!!! YOUR WALKING PATTERN IS DIFFERENT THAN YESTERDAY.")


# In[ ]:




