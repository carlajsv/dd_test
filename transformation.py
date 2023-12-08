import pandas as pd
import requests
from faker import Faker
import re
from datetime import datetime, timedelta




def normalize_column(df, list_columns):
        
    '''
        Function to normalize several columns of a dataFrame.
        
        inputs:
        df = pandas DataFrame
        list_columns = a list from strings referals to columns of df above
    '''
    for i in list_columns:
        
        #normalize column
        df_column = pd.json_normalize(df[i])
        #union dfs
        df_concat = pd.concat([df, df_column], axis=1)
        #delete column from original df
        df_complete = df_concat.drop(i, axis=1)
        df=df_complete
    
    return df


def capitalize_rename_columns(df, columns = None):
    
    '''
        funtion to capitalize and rename (optional) all columns in a Pandas DataFrame.
        Input: 
        df = pandas DataFrame
        columns = list of columns to rename
        
    '''
    #assign the columns of the data frame if no list is entered
    if columns is None:
        columns = df.columns
     
    column_list = []
    for name in columns:
        #add the capitalized names of the columns to the list
        column_list.append(name.upper())
    #rename the columns in df
    df.columns = column_list
    
    return df



def divide_df(df_users, column_name):
    '''
    Divide df_users in two, USERS and COMPANIES
    inputs:
    df_users = df to divide
    column_name = the column from which the df is to be divided
    '''
    
    
    USERS = df_users.loc[:,:column_name]
    COMPANIES = df_users.iloc[:,df_users.columns.get_loc(column_name)-1:]
    
    return USERS, COMPANIES



#Normalize company column from companies_df                                                                
def normalize_column(df, list_columns):
        
    '''
        Function to normalize several columns of a dataFrame where the parameters to be passed are:
        df = pandas DataFrame
        list_columns = a list from strings referals to columns of df above
    '''
    for i in list_columns:
        
        #normalize column
        df_column = pd.json_normalize(df[i])
        #union dfs
        df_concat = pd.concat([df, df_column], axis=1)
        #delete column from original df
        df_complete = df_concat.drop(i, axis=1)
        df=df_complete
    
    return df


#Rename and capitalize names of columns from df
def capitalize_rename_columns(df, columns = None):
    
    '''
        Function to capitalize and rename (optional) all columns in a Pandas DataFrame.
        Input: 
        df = pandas DataFrame
        columns = list of columns to rename
        
    '''
    #assign the columns of the data frame if no list is entered
    if columns is None:
        columns = df.columns
    column_list = []
    for name in columns:
        #add the capitalized names of the columns to the list
        column_list.append(name.upper())
    #rename the columns in df
    df.columns = column_list
    
    return df

#lowercase some colums in a dataframe
def lowercase(df, df_column_list):
    
    '''
        Function to lowercase some columns in DataFrame
        input:
        df_column_list = list of columns to be placed in lowercase 
    
    '''
    for i in df_column_list:
        df[i] = df[i].apply(lambda x: x.lower() if type(x) == str else x)
    return df


###BOOKINGS TRANSFORMATIONS


def create_arrival_date(df, column_day, column_month, column_year, date_format=None):
    
    '''
    function to create the arrival_date column from the three columns day, month and year of arrival
    input:
    df = booking_df
    column_day = column where the days are found 
    column_month = column where the months are found
    column_year = column where the years are found
    date_format= The format in which the columns are, for example: '%Y-%m-%d' (optional) if the format is not passed, 
    the following is set as default: '%Y-%B-%d'.
    '''
    if date_format:
        df['arrival_date'] = pd.to_datetime(df[column_year].astype(str) + '-' +
                                     df[column_month].astype(str) + '-' +
                                     df[column_day].astype(str), format=date_format)

    else:
        df['arrival_date'] = pd.to_datetime(df[column_year].astype(str) + '-' +
                                     df[column_month].astype(str) + '-' +
                                     df[column_day].astype(str), format='%Y-%B-%d')
        
        
        
def get_departure_date(df):
    
    '''
    Function to calculate the departure date column.

    inputs:
    df = booking dataframe
    '''

    #calculate the column 'departure_date' by adding 'stays_in_week_end_nights' and 'stays_in_week_nights'
    df['departure_date'] = df['arrival_date'] + pd.to_timedelta(df['stays_in_weekend_nights'] + df['stays_in_week_nights'], unit='D')
    
    
def reservation_date(df):
    
    '''
    Function to calculate the reservation date column.

    inputs:
    df = bookings dataframe
    '''

    #calculate the reservation date column by removing lead time
    df['reservation_date'] = df['arrival_date'] - pd.to_timedelta(df['lead_time'], unit='D')
    










