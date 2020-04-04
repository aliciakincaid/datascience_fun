#!/usr/bin/env python
# coding: utf-8

# #### Data Science Competition 2020
# Haley Ferguson, Alicia Kincaid, Kelly Krenek

# #### Challenge: 
# Build models for predicting expected flight delays by airline and flight for the **third quarter of 2019**.

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from zipfile import ZipFile


# In[22]:


#import all csv files
air_fares= pd.read_csv("AirFares.csv")
airports = pd.read_csv("Airports.csv")
routes = pd.read_csv("Routes.csv")
flight_description = pd.read_excel("FlightDataDescription(1).xlsx")

#unzip the flight delays file
with ZipFile("FlightDelays.zip","r") as zip_ref:
    #makes a folder in your directory called FlightDelays
    zip_ref.extractall("FlightDelays") 


# In[23]:


#read in the flight delays file to a dataframe
flight_delays = pd.read_csv("FlightDelays/FlightDelays.csv")
#this will take a good amount of time because the file is huge


# In[30]:


flight_delays.tail()


# In[32]:


flight_delays.columns


# Just some observations: 
# avoidable delays- Carrier, Late Aircraft, Departure, Arrival
# unavoidable delys - weather, security, NAS (National Airspace System clearance to fly)

# In[49]:


flight_delays['CANCELED']


# In[54]:


print("Total number of flights canceled from 2018-June 30, 2019:")
flight_delays.loc[flight_delays.CANCELED == 1, "CANCELED"].count()


# In[ ]:




