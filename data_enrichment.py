from faker import Faker
import pandas as pd
import numpy as np
import pycountry




#create random data in users source
def random_users(quantity, users_df):
    '''
        Function to extend the number of users. 
        It can only be used with the users table because it is specific to it 
        and it is only used once in order to increase the number of users that 
        have made reservations in the hotels and to have consistency in the data.
        Also, it create companies id

        Inputs:

        df_users = users DataFrame
        quantity = number of users to be added 
    '''
    #create faker object
    fake = Faker()

    #number of new users
    additional_users = quantity

    new_users = []

    #create random users
    for i in range(additional_users):

        if i == 0:
            user_id = users_df['id'].max() + 1
        else:
            user_id = new_users[i - 1]['id'] + 1

        name = fake.name()
        username = fake.user_name()
        email = fake.email()
        street = fake.street_name()
        suite = fake.random_element(elements=('Apt. 101', 'Suite 202', 'Room 303'))
        city = fake.city()
        zipcode = fake.zipcode()
        lat = fake.latitude()
        lng = fake.longitude()
        phone = fake.phone_number()
        website = fake.url()
        company_name = fake.company()
        company_catchphrase = fake.catch_phrase()
        bs = fake.bs()

        new_record = {
            'id': user_id,
            'name': name,
            'username': username,
            'email': email,
            'address': {
                'street': street,
                'suite': suite,
                'city': city,
                'zipcode': zipcode,
                'geo': {'lat': lat, 'lng': lng}
            },
            'phone': phone,
            'website': website,
            'company': {
                'name': company_name,
                'catchPhrase': company_catchphrase,
                'bs': bs
            }
        }

        #add new record to the list
        new_users.append(new_record)

    #concatenate two dataframes
    users_df_extended = pd.concat([users_df, pd.DataFrame(new_users)], ignore_index=True)
    
    create_id(users_df_extended, 'company_id')

    return users_df_extended


#create ids (id_company to users and id_user to bookings)
def create_id(df, column_id, quantity=None):
    '''
    Creation of random ids in dataframe
    if a specified number of ids is required and the df size exceeds this number, 
    random values between 1 and this specified number will be created, otherwise unique id values will be created for each record.
    
    inputs:
    df: df to which ids are to be added
    column_id: name (str) to be assigned to the new ids column
    quantity(optional): number of ids to be added
    
    '''
    #create faker object
    fake = Faker()
    if quantity:
        df[column_id] = [fake.random_int(min=1, max=quantity) for i in range(len(df))]
    else:
        df[column_id] = np.random.permutation(np.arange(1, len(df) + 1))
        
        
#only some users have companies
def only_some_records(percentage, df, column_id, column_to_modify):
    
    '''
    this function is to be run only once for the purpose that not all customers have companies.
    inputs:
    percentage: fraction of records to be converted to nan, for example: 0.4
    column_id: column id to be considered to eliminate the last records
    column_to_modify: column where we want to delete the records besides the column id
    '''
    
    #number of rows to modify
    num_rows_to_modify = int(percentage * len(df))
    
    #obtain the highest ids to be modified
    id_to_modify = df.nlargest(num_rows_to_modify, column_id)[column_id]
    
    #indentify and replace ids with NaN
    df.loc[df[column_id].isin(id_to_modify), [column_id, column_to_modify]] = [np.nan, np.nan]
    
    
        
############################################## DO NOT USE YET
        
#create country name in bookings    
def get_country_name(country_code):
    '''
    Use pycountry to identify code country in df
    '''
    try:
        country = pycountry.countries.get(alpha_3=country_code)
        if country:
            return country.name
        else:
            country = pycountry.countries.get(alpha_2=country_code)
            return country.name
    except (LookupError, AttributeError):
        return np.nan
    
#get an unique country list from df
def unique_country_list(df_column_w_codes):
    '''
    function to obtain a list of unique countries by passing a df column that has the codes of the countries.
    inputs:
    df_column_w_codes = column with country codes, like df.country_code
    
    '''
    list_countries = list(df_column_w_codes.apply(lambda x: get_country_name(x)).unique())
    return list_countries

#add country column to a df
def add_countries_to_df(df,df_column_w_codes):
    '''
    add to a df a column with country names obtained from a column of another df with country codes
    inputs:
    df = df to which is added the column
    df_column_w_codes = df column with the codes of the countries
    '''
    country_list = unique_country_list(df_column_w_codes)
    
    df['country'] = np.random.choice(country_list, len(df), replace=True)
    
############################################        
        
#create booking id        
def create_booking_id(booking_df):
    
    '''
    Function to add to the df of reservations, the codes of bookings of 
    each record.
    
    inputs:
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
    df['booking_code'] = list(booking_codes)
    
    #union of two df
    booking_with_codes = pd.concat([df,booking_df], axis=1)
    
    return booking_with_codes
    









