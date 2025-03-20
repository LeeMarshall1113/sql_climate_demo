#!/usr/bin/env python

"""
SQL Demo: Demonstrating data science proficiency with Python & SQL (SQLite).
- Create an in-memory database.
- Create & populate a 'climate_data' table.
- Run advanced queries (aggregations, window functions, CTE).
- Load results into Pandas for further analysis.
"""

import sqlite3
import pandas as pd

def create_and_populate_db(connection):
    """
    Creates a table named 'climate_data' and inserts sample records.
    """
    # Create table (if not exists)
    create_table_query = """
    CREATE TABLE IF NOT EXISTS climate_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        reading_date TEXT NOT NULL,
        temperature FLOAT NOT NULL,
        humidity FLOAT NOT NULL
    );
    """
    connection.execute(create_table_query)

    # Insert some sample data
    # For demonstration, these dates and temps are fictional.
    records = [
        ("New York",  "2025-01-01",  -5.2,  35.0),
        ("New York",  "2025-01-02",  -2.1,  40.0),
        ("New York",  "2025-01-03",   0.5,  42.0),
        ("Chicago",   "2025-01-01",  -7.0,  50.0),
        ("Chicago",   "2025-01-02",  -5.5,  55.0),
        ("Chicago",   "2025-01-03",  -3.2,  48.0),
        ("Houston",   "2025-01-01",  10.2,  70.0),
        ("Houston",   "2025-01-02",  12.1,  68.0),
        ("Houston",   "2025-01-03",  15.0,  65.0),
        ("San Diego", "2025-01-01",  15.2,  55.0),
        ("San Diego", "2025-01-02",  16.5,  52.0),
        ("San Diego", "2025-01-03",  18.0,  50.0),
    ]

    insert_query = """
    INSERT INTO climate_data (city, reading_date, temperature, humidity)
    VALUES (?, ?, ?, ?)
    """
    connection.executemany(insert_query, records)
    connection.commit()


def run_basic_analytics(connection):
    """
    Runs some basic SQL queries (aggregations) to demonstrate proficiency.
    """
    # 1. Average temperature & humidity by city
    query_avg = """
    SELECT 
        city,
        AVG(temperature) AS avg_temp,
        AVG(humidity) AS avg_humidity
    FROM climate_data
    GROUP BY city
    ORDER BY avg_temp DESC;
    """
    df_avg = pd.read_sql_query(query_avg, connection)
    print("=== Average Temperature & Humidity by City ===")
    print(df_avg, "\n")


def run_advanced_analytics(connection):
    """
    Demonstrates more advanced SQL: 
    - Window functions (ranking cities by temperature per day).
    - CTE (common table expression) to filter top temperatures.
    """
    # 2A. Use a window function to rank temperatures by city (within each date)
    query_window = """
    SELECT
        city,
        reading_date,
        temperature,
        RANK() OVER (
            PARTITION BY reading_date
            ORDER BY temperature DESC
        ) AS temp_rank
    FROM climate_data
    ORDER BY reading_date, temp_rank;
    """
    df_window = pd.read_sql_query(query_window, connection)
    print("=== Window Function: Temperature Rank per Date ===")
    print(df_window, "\n")

    # 2B. CTE Example: retrieve only the top 1 city per day (highest temperature)
    query_cte = """
    WITH ranked_temps AS (
        SELECT
            city,
            reading_date,
            temperature,
            RANK() OVER (
                PARTITION BY reading_date
                ORDER BY temperature DESC
            ) AS temp_rank
        FROM climate_data
    )
    SELECT *
    FROM ranked_temps
    WHERE temp_rank = 1
    ORDER BY reading_date;
    """
    df_cte = pd.read_sql_query(query_cte, connection)
    print("=== CTE: Hottest City per Date ===")
    print(df_cte, "\n")


def main():
    # 1. Create in-memory SQLite database & connect
    conn = sqlite3.connect(":memory:")
    
    # 2. Create and populate table
    create_and_populate_db(conn)

    # 3. Basic analytics
    run_basic_analytics(conn)

    # 4. Advanced analytics (window functions, CTE)
    run_advanced_analytics(conn)

    # 5. (Optional) Additional Data Science Steps in Pandas
    # Suppose we want to do a quick correlation or summary on the entire table:
    df_all = pd.read_sql_query("SELECT * FROM climate_data;", conn)
    print("=== Full climate_data Table in Pandas ===")
    print(df_all.head(), "\n")
    
    # Example: correlation between temperature and humidity
    corr = df_all[["temperature", "humidity"]].corr()
    print("=== Correlation Matrix between Temperature & Humidity ===")
    print(corr)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()
