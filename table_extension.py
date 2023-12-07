from faker import Faker
import pandas as pd
import numpy as np

def create_company_id(users_df):
    users_df['company_id'] = np.random.permutation(np.arange(1, len(users_df) + 1))
    
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
    
    create_company_id(users_df_extended)

    return users_df_extended







