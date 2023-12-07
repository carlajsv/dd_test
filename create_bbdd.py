##DDBB
import sqlite3


def db():
    #connect to DDBB
    return sqlite3.connect("bookings.db")


def create_tables():
    '''
    function to create tables in the ddbb
    '''
   
    cursor = db().cursor()
    
    #creation of each of the tables in ddbb
    
    #raw_users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS raw_users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            username TEXT,
            email TEXT,
            address TEXT,
            country TEXT,
            phone TEXT,
            website TEXT,
            company TEXT,
            company_id INTEGER,
            FOREIGN KEY (company_id) REFERENCES COMPANIES(COMPANY_ID)
        )
    ''')
    
    #raw_bookings
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS raw_bookings (
            user_id INTEGER,
            booking_id INTEGER PRIMARY KEY,
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
            FOREIGN KEY (user_id) REFERENCES raw_users(id)
        )
    ''')

    #USERS
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS USERS (
            USER_ID INTEGER PRIMARY KEY,
            USER_NAME TEXT,
            USER_EMAIL TEXT,
            USER_ADDRESS TEXT,
            USER_COUNTRY_ID INTEGER,
            USER_PHONE TEXT,
            USER_WEBSITE TEXT,
            COMPANY_ID INTEGER,
            
            FOREIGN KEY (USER_COUNTRY_ID) REFERENCES COUNTRIES(COUNTRY_ID),
            FOREIGN KEY (COMPANY_ID) REFERENCES COMPANIES(COMPANY_ID)
        )
    ''')

    #COMPANIES
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS COMPANIES (
            COMPANY_ID INTEGER PRIMARY KEY,
            USER_ID INTEGER,
            COMPANY_NAME TEXT,
            FOREIGN KEY (USER_ID) REFERENCES USERS(USER_ID)
        )
    ''')

    #HOTELS
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS HOTELS (
            HOTEL_ID INTEGER PRIMARY KEY,
            HOTEL_NAME TEXT
        )
    ''')

    #AGENTS
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS AGENTS (
            AGENT_ID INTEGER PRIMARY KEY,
            AGENT_NAME TEXT
        )
    ''')

    #MEAL_TYPES
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MEAL_TYPES (
            MEAL_ID INTEGER PRIMARY KEY,
            MEAL_NAME TEXT
        )
    ''')

    #ROOM_TYPES
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ROOM_TYPES (
            ROOM_ID INTEGER PRIMARY KEY,
            ROOM_NAME TEXT
        )
    ''')
    
    #COUNTRIES
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS COUNTRIES (
            COUNTRY_ID INTEGER PRIMARY KEY,
            COUNTRY TEXT
        )
    ''')
    

    #BOOKINGS
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS BOOKINGS (
            BOOKING_ID INTEGER PRIMARY KEY,
            USER_ID INTEGER,
            HOTEL_ID INTEGER,
            ARRIVAL_DATE TEXT,
            DEPARTURE_DATE TEXT,
            RESERVATION_DATE TEXT,
            ADULTS INTEGER,
            CHILDREN INTEGER,
            MEAL_ID INTEGER,
            COUNTRY_ID INTEGER,
            RESERVED_ROOM_TYPE_ID INTEGER,
            ASSIGNED_ROOM_TYPE_ID INTEGER,
            AGENT_ID INTEGER,
            STATUS TEXT,
            LAST_UPDATED_AT TEXT,
            
            FOREIGN KEY (USER_ID) REFERENCES USERS(USER_ID)
            FOREIGN KEY (HOTEL_ID) REFERENCES HOTELS(HOTEL_ID),
            FOREIGN KEY (MEAL_ID) REFERENCES MEAL_TYPES(MEAL_ID),
            FOREIGN KEY (COUNTRY_ID) REFERENCES COUNTRIES(COUNTRY_ID),
            FOREIGN KEY (RESERVED_ROOM_TYPE_ID) REFERENCES ROOM_TYPES(ROOM_ID),
            FOREIGN KEY (ASSIGNED_ROOM_TYPE_ID) REFERENCES ROOM_TYPES(ROOM_ID),
            FOREIGN KEY (AGENT_ID) REFERENCES agents(AGENT_ID)
        )
    ''')

    #save changes
    db().commit()

        
        
