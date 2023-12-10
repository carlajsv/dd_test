# DD PROJECT

## Hello

In this repository you can find my project in which I make an E2E work from an extraction of user data through an API and a `.csv` document containing hotel reservations data in which I had to enrich with random data to be able to have concordance when relating tables.

In terms of language to perform the extraction, transformation and loading of the data I used Python, as a database I used SQLite and as a visualization tool I used QlikSense.

In this repository there are also several files: 

- **main.ipynb**: This is the file where you run a simulation of the ETL process that is performed to the tables, including data enrichment and data cleansing.

The `.py` files contain the functions created to perform the above process:

- **Get_data_api.py**: contains the functions with which the download of the data from the users table was done.

- **Data_enrichment.py**: contains all the functions created to enrich the data.

- **Dim_tables.py**: contains the functions that helped me to create my dimension tables.

- **Transformation.py** : contains the transformation functions that were applied to each of the tables.

- **clean.py** : contains the functions to clean the data.

Then there are the csv files containing the initial data sources.

- **Raw_bookings.csv** : keeps the data exactly as it was found.

- **Raw_users.csv** : keeps the data exactly as it was extracted from the API.

- **Raw_users_extended**: keeps the same structure as `Raw_users.csv` but with much more data added and with one more column called company_id.

- **Raw_bookings_extended**: keeps the same structure as Raw_bookings.csv but with one more column, named users_id

Finally, there is the **dd_test.db** file which is the database created only for the purposes of this project and which contains all the raw and clean data stored and acts as DWH.
