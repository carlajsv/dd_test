import pandas as pd
import requests
import sqlite3


def db():
    #connect to DDBB
    connection = sqlite3.connect("bookings.db")
    #cursor
    cursor = conexion.cursor()
    return cursor

def consult_table(table_name=None):
    '''
    queries an sql table in the database and returns it as dataframe
    
    '''
    if table_name:
        query = f"SELECT * FROM {table_name}"
        db().execute(query)
        #get query result
        results = cursor.fetchall()
        #convert into df
        results_df = pd.DataFrame(results)
    results_df = None
    return results_df
    

def only_new_records(column_ID, new_df, old_df):
    '''
    Function to recognize records that are not in an existing df.
    inputs:
    column_ID = column to be used to compare both df 
    new_df = df of records to be added
    odl_df = existing dataframe
    
    outputs: df with new and non-existent records
    
    '''
    
    #leftjoin and only the records that do not exist in the old df
    new_records = pd.merge(new_df, old_df, on=[column_ID], how='left', indicator=True).query('_merge == "left_only"').drop('_merge', axis=1)
    return registros_nuevos



def get_api_data(url):
    
    '''
       gets data from the api.
       
       inputs:
       url = url from jsonplaceholder API
       
       output:
       df with api data
    '''
    response = requests.get(url)
    #convert into json format
    data = response.json()
    #conver to df format
    api_df = pd.DataFrame(data)
    return api_df
    
    
def add_data(url, old_table = None, ID_old_table = None):
    '''
    adds the new data, if any, to the existing table and generates a df with the completed data
    '''
    old_df = consult_table(old_table)
    new_df = get_api_data(url)
    
    if old_df:
        #get only new records
        new_records = only_new_records(ID_old_table, new_df, old_df)
        #add new records to df
        new_df = pd.concat([old_df, new_records], ignore_index=True)
    
    return new_df
    
    

  