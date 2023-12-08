import pandas as pd
from faker import Faker
import re
import numpy as np
import data_enrichment as de


def create_dim_users_table(df_users):
    '''
    function to create a dim_users table
    
    inputs:
    df_users = df with users raw data and extended. 
    '''
    #Split the users from the first column to the company column.
    dim_users = df_users.loc[:,:'website']
    
    return dim_users


def create_dim_companies_table(df_users, column_name):
    '''
    function to create a dim_companies table
    
    inputs:
    df_users = df with users raw data and extended. 
    '''
    #split users_df from the company column onward
    dim_companies = df_users.iloc[:,df_users.columns.get_loc('company'):]
    
    return dim_companies



def create_dim_agent_table():
    
    '''
    Function to create the agents dimension table
    '''
    
    #faker object
    fake = Faker()
    
    #generate random data
    agent_data = {
        'AGENT_ID': list(range(1, 11)),
        'AGENT_NAME': [fake.name() for i in range(10)]
    }

    #create agent_df
    dim_agents = pd.DataFrame(agent_data)

    return dim_agents


def create_dim_country_table():
    
    '''
    function to create the country_dim table
    '''
    
    #define the list with the code_country present in bookings_df
    list_code_country = ['RUS','PRT','ARG','FRA','GBR','DEU','BRA','IRL','USA','KOR','ESP','DNK','CHN','NLD','HUN',
 'POL','CN','BEL','LUX','AUT','CHE','ARE','ITA','FIN','TUN','NOR','ROU','JAM','ALB','AUS','SWE',
 'HRV','HKG','IND','ISR','CZE','IRN','GEO','DZA','MAR','AND','TUR','MOZ','ZAF','GIB','URY','BLR',
 'EST','LTU','JEY','CAF','CYP','GRC','LVA','COL','GGY','KWT','CUB','UKR','CMR','MYS','THA','NZL',
 'BIH','MUS','NGA','COM','OMN','SUR','MEX','CHL','UGA','BGR','CIV','SRB','DOM','JOR','SYR','PHL',
 'PRI','JPN','SGP','ARM','BDI','AGO','SAU','LBN','VNM','AZE','SVN','PLW','QAT','EGY','PER','SVK',
 'CPV','MDV','MLT','MWI','ECU','VEN','IRQ','SEN','IDN','TWN','HND','RWA','PAK','ZMB','KHM','MCO',
 'BGD','ISL','UZB','KAZ','IMN','TJK','NIC','BEN','MAC','VGB','CRI','TZA','GAB','MKD','GHA','TMP',
 'GLP','KEN','BFA','LKA','LBY','PAN','GNB','MLI','BHR','NAM','BOL','SYC','PRY','BRB','ABW','AIA',
 'SLV','DMA','PYF','LIE','GUY','LCA','ATA','MNE']
    
    #save in dict all countries
    countries = {
    'COUNTRY_ID' : list_code_country,
    'COUNTRY_NAME':[de.get_country_name(i) for i in list_code_country]
    }
    
    #convert in DataFrame
    dim_countries = pd.DataFrame(countries)
    
    return dim_countries



def create_dim_meal_table():
    
    '''
    function to create the meal_dim table
    '''
    
    #define the list with the meal_code present in bookings_df
    list_code_meal = ['BB', 'HB', 'FB', 'SC', 'Undefined']
    #define the list with the meal_name 
    list_name_meal = ['Bed and Breakfast', 'Half board', 'Full board', 'no meal package', 'no meal package']
    
    #save in dict all meals
    meals = {
    'MEAL_ID' : list_code_meal,
    'MEAL_NAME': list_name_meal
    }
    
    #convert in DataFrame
    dim_meals = pd.DataFrame(meals)
    
    return dim_meals


def create_dim_hotel_table():
    
    '''
    function to create the hotel_dim table
    '''
    
    #define the list with the hotel code 
    list_code_hotel = ['RH', 'CH']
    #define the list with the hotel_name present in bookings_df
    list_name_hotel = ['Resort Hotel', 'City Hotel']
    
    #save in dict all hotels
    hotels = {
    'HOTEL_ID' : list_code_hotel,
    'HOTEL_NAME': list_name_hotel
    }
    
    #convert in DataFrame
    dim_hotels = pd.DataFrame(hotels)
    
    return dim_hotels

