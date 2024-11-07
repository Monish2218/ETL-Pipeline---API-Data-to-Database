# ETL Pipeline: API to PostgreSQL

## Overview
This project demonstrates an ETL pipeline that extracts data from a public API, transforms it, and loads it into a PostgreSQL database.

## Steps
1. **Extract**: Fetches random user data from the RandomUser API.
2. **Transform**: Converts the JSON data to a DataFrame and selects specific columns.
3. **Load**: Loads the transformed data into a PostgreSQL table named `random_users`.

## Requirements
- Python 3.x
- PostgreSQL
- Python packages: `requests`, `pandas`, `sqlalchemy`

## Usage
1. Update `DATABASE_URL` in the code with your PostgreSQL credentials.
2. Run `etl_api_to_postgres.py`.
