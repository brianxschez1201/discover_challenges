#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Imports...
import numpy as np
import pandas as pd # To read in the data.
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt # To visualize results.


# In[3]:


# Getting the initial inputs.
initial_input = input("Enter...\n" +
                      "1) The amount of money you can spend today.\n" +
                      "2) The number of different stocks available for buying or selling.\n" +
                      "3) The number of remaining days for trading stocks.\n" +
                      "Please enter sequentially on one line with each value delimited by spaces:")


# In[4]:


# Splitting the input to get...
# The funds for today.
# The number of available stocks for buying and selling.
# The number of remaining days for trading stocks.
initial_input_split = initial_input.split()

funds_for_today = float(initial_input_split[0])
num_available_stocks = int(initial_input_split[1])
remaining_days = int(initial_input_split[2])


# In[6]:


# Now we use a loop to create files for each available stock...

# A list that will store the names of the stocks so that we can access their
# files later...
stock_names = list()
# Shares list correspond to stock names.
shares_list = list()

# Getting the input for each stock.
for stock in range(1,num_available_stocks+1) :
    stock_input = input("\nStock " + str(stock) + "\n" +
                        "Enter...\n" +
                        "1) The name of the stock.\n" +
                        "2) The number of shares you own of that stock.\n" +
                        "3) The stock's prices for the last 5 days separated by spaces.\n" +
                        "Please enter sequentially on one line with each value delimited by spaces:")
    
    
    # Splitting the input to get...
    # 1) The name of the stock.
    # 2) The number of shares you own of that stock.
    # 3) 5 space separated numbers representing the stock's price for the last 5 days.
    stock_input_split = stock_input.split()
    
    # Get the name, store it in the list of stock names, and create a file for the stock with that name.
    name = stock_input_split[0]
    stock_names.append(name)
    stock_file = open(name +".txt", "w")
    
    # Stores the number of shares owned into a list.
    shares_owned = int(stock_input_split[1])
    shares_list.append(shares_owned)
    
    # Writing labels to the file...
    stock_file.write("day, price\n")
    
    # Write to the stock's file the previous days (1-5) accompanied by the stock's price that day.
    stock_file.write("1," + stock_input_split[2] + "\n")
    stock_file.write("2," + stock_input_split[3] + "\n")
    stock_file.write("3," + stock_input_split[4] + "\n")
    stock_file.write("4," + stock_input_split[5] + "\n")
    stock_file.write("5," + stock_input_split[6])
    
    stock_file.close()


# In[7]:


dataframe = pd.read_csv("Apple.txt")
dataframe


# In[13]:


current_day = 6

for day in range(1,remaining_days+1) :
    for stock_index in range(0,len(stock_names)) :
        
        name = stock_names[stock_index]
        shares_owned = shares_list[stock_index]
        
        dataframe = pd.read_csv("Apple.txt")
        
        # I don't know how this part works.
        X = dataframe.iloc[:,0].values.reshape(-1,1) 
        Y = dataframe.iloc[:,1].values.reshape(-1,1)
        
        model = LinearRegression()
        model.fit(X,Y)
        
        x_predict = np.array([[current_day]])
        y_predict = model.predict(x_predict)
        print(y_predict)
        
        current_day += 1


# In[ ]:




