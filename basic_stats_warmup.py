#!/usr/bin/env python
# coding: utf-8

# In[12]:


import math
from scipy.stats import t

def find_mean(integer_list) :
    sum = 0
    for integer in integer_list :
        sum += integer
    mean = sum / len(integer_list)
    return mean

integers = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]

print(find_mean(integers))


# In[17]:


def find_median(integer_list) :
    integer_list.sort()
    if len(integer_list) % 2 == 0 :
        first_middle_int = integer_list[int((len(integer_list) / 2) - 1)]
        second_middle_int = integer_list[int(len(integer_list) / 2)]
        median = (first_middle_int + second_middle_int) / 2
        return median
    else :
        median = integer_list[int(len(integer_list) / 2)]
        return median
print(find_median(integers))


# In[18]:


def find_mode(integer_list) :
       counts = dict()
       mode = None
       mode_count = None
       for integer in integer_list :
           counts[integer] = counts.get(integer, 0) + 1
       for k, v in counts.items() :
           if(mode_count is None or v > mode_count) :
               mode = k
               mode_count = v
       return mode
   
print(find_mode(integers))           


# In[19]:


def find_standard_deviation(integer_list) :
    mean = find_mean(integer_list)
    squared_differences = list()
    for integer in integers :
        squared_differences.append((mean - integer) ** 2)
    mean_squared_differences = find_mean(squared_differences)
    sd = math.sqrt(mean_squared_differences)
    return sd

print(find_standard_deviation(integers))


# In[17]:


def find_confidence_intervals(integer_list, confidence) :
    mean = find_mean(integer_list)
    sd = find_standard_deviation(integer_list)
    n = len(integer_list) ## Sample size...
    standard_error = sd / math.sqrt(sample_size)
    ## Unfinished...
    

