import pandas as pd
import requests


def get_save_data(url, name_csv):
    
    '''
        get the data from the API and save it in raw form in a .csv document.
        return a DataFrame
        The necessary parameters for this function are:

        url= The API url
        name_csv = the name of the document with ".csv" at the end
    '''
    response = requests.get(url)
    #Convert to json format
    data = response.json()
    #conver to df format
    data_df = pd.DataFrame(data)
    #save into .csv
    data_df.to_csv(name_csv, index=False)
    return data_df

def normalize_column(df, list_columns):
        
    '''
        Function to normalize several columns of a dataFrame where the parameters to be passed are:
        df = a pandas dataframe
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






    