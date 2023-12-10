##DDBB
import sqlite3
from sqlite3 import Error

#Create connection to a ddbb
def create_connection(db_file):
    ''' 
    
    create a database connection to the SQLite database specified by db_file
    db_file: database file
    return:
    Connection object or None
    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn
    
    
    

def create_table(conn, create_table_sql):
    ''' 
    create a table from the create_table_sql statement
    
    Inputs:
    conn = Connection object
    create_table_sql = a CREATE TABLE statement
    
    '''
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

#create the bookings database and all tables belonging to it
def main():
    
    #assign name and path of the bbdd
    database = r"./bookings.db"

    sql_create_raw_users = """CREATE TABLE IF NOT EXISTS raw_users (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT,
                                    username TEXT,
                                    email TEXT,
                                    address TEXT,
                                    phone TEXT,
                                    website TEXT,
                                    company TEXT,
                                    company_id NUMERIC,
                                    FOREIGN KEY (company_id) REFERENCES COMPANIES(COMPANY_ID)
                                );"""

    sql_create_raw_bookings = """CREATE TABLE IF NOT EXISTS raw_bookings (
                                booking_code INTEGER PRIMARY KEY,
                                Hotel TEXT,
                                Is_canceled INTEGER,
                                lead_time INTEGER,
                                arrival_date_year INTEGER,
                                arrival_date_month INTEGER,
                                arrival_date_day_of_month INTEGER,
                                stays_in_weekend_nights INTEGER,
                                stays_in_week_nights INTEGER,
                                adults INTEGER,
                                children INTEGER,
                                meal TEXT,
                                country TEXT,
                                is_repeated_guest INTEGER,
                                previous_cancellations INTEGER,
                                previous_bookings_not_canceled INTEGER,
                                reserved_room_type TEXT,
                                assigned_room_type TEXT,
                                agent INTEGER,
                                reservation_status TEXT,
                                reservation_status_date TEXT,
                                user_id INTEGER,
                                FOREIGN KEY (user_id) REFERENCES raw_users(id)
                            );"""
    
    sql_create_dim_users = """CREATE TABLE IF NOT EXISTS DIM_USERS (
                                    USER_ID INTEGER PRIMARY KEY,
                                    USER_NAME TEXT,
                                    USER_EMAIL TEXT,
                                    USER_ADDRESS TEXT,
                                    USER_PHONE TEXT,
                                    USER_WEBSITE TEXT,
                                    COMPANY_ID INTEGER,
                                    FOREIGN KEY (COMPANY_ID) REFERENCES COMPANIES(COMPANY_ID)
                                );"""
    
    sql_create_dim_companies = """CREATE TABLE IF NOT EXISTS DIM_COMPANIES (
                                    COMPANY_ID INTEGER PRIMARY KEY,
                                    USER_ID INTEGER,
                                    COMPANY_NAME TEXT,
                                    FOREIGN KEY (USER_ID) REFERENCES USERS(USER_ID)
                                );"""
    
    sql_create_dim_hotels = """CREATE TABLE IF NOT EXISTS HOTELS (
                                    HOTEL_ID INTEGER PRIMARY KEY,
                                    HOTEL_NAME TEXT
                                );"""
    
    sql_create_dim_agents = """CREATE TABLE IF NOT EXISTS AGENTS (
                                    AGENT_ID INTEGER PRIMARY KEY,
                                    AGENT_NAME TEXT
                                );"""
    
    sql_create_dim_meals = """CREATE TABLE IF NOT EXISTS MEAL_TYPES (
                                MEAL_ID INTEGER PRIMARY KEY,
                                MEAL_NAME TEXT
                                );"""
    
    sql_create_dim_countries = """CREATE TABLE IF NOT EXISTS COUNTRIES (
                                    COUNTRY_ID TEXT PRIMARY KEY,
                                    COUNTRY TEXT
                                );"""
    
    sql_create_bookings = """CREATE TABLE IF NOT EXISTS BOOKINGS (
                                BOOKING_CODE INTEGER PRIMARY KEY,
                                USER_ID INTEGER,
                                COUNTRY_ID INTEGER,
                                AGENT_ID INTEGER,
                                HOTEL_ID INTEGER,
                                ADULTS INTEGER,
                                CHILDREN INTEGER,
                                MEAL_ID INTEGER,
                                RESERVED_ROOM_TYPE_ID INTEGER,
                                ASSIGNED_ROOM_TYPE_ID INTEGER,
                                STATUS TEXT,
                                LAST_UPDATED_AT TEXT,
                                ARRIVAL_DATE TEXT,
                                DEPARTURE_DATE TEXT,
                                RESERVATION_DATE TEXT,
                                FOREIGN KEY (USER_ID) REFERENCES USERS(USER_ID),
                                FOREIGN KEY (HOTEL_ID) REFERENCES HOTELS(HOTEL_ID),
                                FOREIGN KEY (MEAL_ID) REFERENCES MEAL_TYPES(MEAL_ID),
                                FOREIGN KEY (COUNTRY_ID) REFERENCES COUNTRIES(COUNTRY_ID),
                                FOREIGN KEY (RESERVED_ROOM_TYPE_ID) REFERENCES ROOM_TYPES(ROOM_ID),
                                FOREIGN KEY (ASSIGNED_ROOM_TYPE_ID) REFERENCES ROOM_TYPES(ROOM_ID),
                                FOREIGN KEY (AGENT_ID) REFERENCES agents(AGENT_ID)
                            );"""
    
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        #create raw_users table
        create_table(conn, sql_create_raw_users)

        #create raw_bookings table
        create_table(conn, sql_create_raw_bookings)

        #create dim_users table
        create_table(conn, sql_create_dim_users)

        #create dim_companies table
        create_table(conn, sql_create_dim_companies)

        #create dim_hotels table
        create_table(conn, sql_create_dim_hotels)

        #create dim_agents table
        create_table(conn, sql_create_dim_agents)

        #create dim_meals table
        create_table(conn, sql_create_dim_meals)

        #create dim_countries table
        create_table(conn, sql_create_dim_countries)

        #create bookings table
        create_table(conn, sql_create_bookings)
    else:
        print("Error! cannot create the database connection.")
        
        
        
def insert_table_sql(table, name_sql_table, db_file):
    '''
    Creates table in sqldb from Pandas DataFrame
    '''
    conn = create_connection(db_file)
    table = table.fillna('')
    table.to_sql(name_sql_table, conn, if_exists='append', index = False)