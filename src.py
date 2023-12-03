import pandas as pd
import requests


def get_save_data(url,name_csv,df=None,id_column=None):
    
    '''
       gets the data from the api and in case it gets new records, 
       it adds them without duplicating the previous ones, as well as 
       creates a csv file and saves it.
       
       inputs:
       url = url from jsonplaceholder API
       name_csv = name for the csv file
       df = if any, df in which data has been stored in previous requests
       id_column = primary key or id to compare new and old records
       
       output:
       df with all data
       csv with all data
    '''
    response = requests.get(url)
    #Convert into json format
    data = response.json()
    #conver to df format
    data_df = pd.DataFrame(data)
        
    if df is not None and id_column is not None:
        new_records = data_df[~data_df[id_column].isin(df[id_column])]
        df = pd.concat([df, new_records], ignore_index=True)
        #save into .csv
        df.to_csv(name_csv, index=False)
        return df
    else:
        #save into .csv
        data_df.to_csv(name_csv, index=False)
        return data_df      
    
    


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

def remove_chars(df, column):
    
    '''
       removes several special characters from a particular column
       inputs:
       df = pandas DataFrame
       column = a string name of a column
    '''
    #list of charts to removes
    chars = ['-', 'x', ')', '(', '.', ' ']
    #remove chars
    for i in chars:
        df[column] = df[column].apply(lambda string: string.replace(i, ''))


def lowercase(df):
    
    '''
        lower case all data frame data
        input:
        df = pandas DataFrame
    
    '''
    df = df.applymap(lambda x: x.lower() if type(x) == str else x)
    return df


    