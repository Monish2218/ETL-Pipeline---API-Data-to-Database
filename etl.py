import requests
import pandas as pd
from sqlalchemy import create_engine

# Database connection string
DATABASE_URL = "postgresql://username:password@localhost:5432/etl_db"

# API URL for random user data
API_URL = "https://randomuser.me/api/?results=5"

# Step 1: Extract - Fetch data from API
def extract_data():
    try:
        response = requests.get(API_URL)
        data = response.json()['results']
        print("Data extracted successfully")
        return data
    except Exception as e:
        print("Error extracting data:", e)

# Step 2: Transform - Convert to DataFrame and select required columns
def transform_data(data):
    df = pd.json_normalize(data)
    df = df[['name.first', 'name.last', 'email', 'dob.age']]
    df.columns = ['first_name', 'last_name', 'email', 'age']
    print("Data transformed successfully")
    return df

# Step 3: Load - Load data into PostgreSQL
def load_data(df):
    engine = create_engine(DATABASE_URL)
    try:
        df.to_sql('random_users', engine, if_exists='replace', index=False)
        print("Data loaded successfully")
    except Exception as e:
        print("Error loading data:", e)

if __name__ == "__main__":
    data = extract_data()
    df = transform_data(data)
    load_data(df)
