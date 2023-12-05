import pandas as pd
import requests
from faker import Faker
import re
import phonenumbers


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
    chars = ['-','x',')','(', '.', ' ', '+']
    #remove chars
    for i in chars:
        df[column] = df[column].apply(lambda string: string.replace(i, ''))


def lowercase(df):
    
    '''
        lower case all data frame data
        input:
        df = pandas DataFrame
    
    '''
    df = df.map(lambda x: x.lower() if type(x) == str else x)
    return df


def random_users(quantity, df_users):
    '''
        Function to extend the number of users. 
        It can only be used with the users table because it is specific to it 
        and it is only used once in order to increase the number of users that 
        have made reservations in the hotels and to have consistency in the data.

        Inputs:

        df_users = users DataFrame
        quantity = number of users to be added 
    '''
    #faker object
    fake = Faker()

    #number of new users
    additional_users = quantity

    for _ in range(additional_users):
        user_id = df_users['USER_ID'].max() + 1  #get unique ID
        user_name = fake.name()
        user_username = fake.user_name()
        user_email = fake.email()
        user_phone = fake.phone_number()
        website = fake.url()
        user_street = fake.street_address()
        user_suite = fake.secondary_address()
        user_city = fake.city()
        user_zipcode = fake.zipcode()
        user_lat = fake.latitude()
        user_lng = fake.longitude()

        new_user = [
            user_id,
            user_name,
            user_username,
            user_email,
            user_phone,
            website,
            user_street,
            user_suite,
            user_city,
            user_zipcode,
            user_lat,
            user_lng,
        ]

        new_user_df = pd.DataFrame([new_user], columns=df_users.columns)

        #concatenate two dataframes
        df_users = pd.concat([df_users, new_user_df], ignore_index=True)

    #create a .csv file
    df_users.to_csv('users_extended.csv', index=False)

    return df_users




def random_companies(quantity_users, quantity_companies, df_companies):
    
    '''
    This function is used only once, it is used to extend the df_companies we have 
    with random data, add a user id and a company id to them.
    
    inputs:
    quantity_companies = number of companies
    quantity_users = total number of users we have in our user database
    
    important: the number of users must be greater than the number of companies
    '''
    #faker object
    fake = Faker()

    #obtain current unique USER_ID and COMPANY_ID
    existing_user_ids = set(df_companies['USER_ID'].unique())
    existing_company_ids = set(df_companies['COMPANY_ID'].unique())

    new_records = []

    #generate additional records
    for _ in range(quantity_companies):
        #generate unique USER_ID
        user_id = fake.random_int(min=1, max=quantity_users)
        while user_id in existing_user_ids:
            user_id = fake.random_int(min=1, max=quantity_users)

        #generate unique COMPANY_ID
        company_id = max(existing_company_ids) + 1
        while company_id in existing_company_ids:
            company_id += 1

        #update existing USER_ID and COMPANY_ID sets
        existing_user_ids.add(user_id)
        existing_company_ids.add(company_id)

        #generate random data
        company_name = fake.company()
        company_catchphrase = fake.catch_phrase()
        company_bs = fake.bs()

        #create new record
        new_record = {
            'COMPANY_ID': company_id,
            'USER_ID': user_id,
            'COMPANY_NAME': company_name,
            'COMPANY_CATCHPHRASE': company_catchphrase,
            'COMPANY_BS': company_bs
        }

        new_records.append(new_record)

    #concatenate new records to existing DataFrame
    df_companies_extended = pd.concat([df_companies, pd.DataFrame(new_records)], ignore_index=True)

    #sort DataFrame by 'COMPANY_ID'
    df_companies_extended.sort_values(by='COMPANY_ID', inplace=True)

    #save DataFrame to a CSV file
    df_companies_extended.to_csv('companies_extended.csv', index=False)

    return df_companies_extended



def clean_user_street(street):
    '''
    Function to clean the column 'USER_STREET'
    input:
    street = string
    
    '''
    #remove from text 'Suite' or 'Apt' and the numbers following it
    cleaned_street = re.sub(r'\b(Suite|Apt)\.?\s*\d+', '', street)
    return cleaned_street.strip()




def add_https(website):
    '''
    Function to add https prefix to website str
    input:
    website = string
    
    '''
    if not website.startswith('http'):
        return 'https://www.' + website
    else:
        return website
    
    
    
def add_bookings_code(quantity_users, booking_df):
    
    '''
    Function to add to the df that we have of reservations, the codes of reservations of 
    each registry and the users id of the users that made the reservation.
    
    inputs:
    quantity_users = total number of users we have in our user database
    booking_df = df of reserves
    '''
    #faker object
    fake = Faker()
    
    #empty df
    df = pd.DataFrame()
    
    #empty booking set
    booking_codes = set()
    
    while len(booking_codes) < len(booking_df):
        booking_code = fake.vin()
        booking_codes.add(booking_code)
    
    #create booking_code column
    df['BOOKING_CODE'] = list(booking_codes)
    #create user_id column
    df['USER_ID'] = [fake.random_int(min=1, max=quantity_users) for i in range(len(booking_df))]
    
    #union of two df
    booking_with_codes_df = pd.concat([df,booking_df], axis=1)


    return booking_with_codes_df



    