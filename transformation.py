import pandas as pd
import requests
from faker import Faker
import re




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

creat










