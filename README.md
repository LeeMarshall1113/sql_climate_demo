SQL Demo: Climate Data Analysis

A minimal demonstration of Python + SQL proficiency, using an in-memory SQLite database and a sample climate dataset. The script showcases:

    Database Creation & Population – Creates a climate_data table and inserts records.
    Basic SQL Analytics – Uses GROUP BY to compute average temperature and humidity by city.
    Advanced SQL Features – Demonstrates window functions (RANK()) and a Common Table Expression (CTE) to find top temperatures per day.
    Integration with Pandas – Pulls query results into a Pandas DataFrame for additional data science tasks (e.g., correlation analysis).

Requirements

    Python 3.7+
    pandas (for reading query results into a DataFrame)

(You don’t need to install SQLite separately; it’s bundled with Python.)
Installation

    Clone or download this repository (if it’s in one). Otherwise, just save the script as sql_climate_demo.py (or similar).
    (Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

Install Pandas (if not already):

    pip install pandas

Usage

    Run the script:

    python sql_climate_demo.py

    Observe the console output:
        Tables showing average temperature by city.
        Ranked temperatures within each date using window functions.
        CTE output for top temperature per date.
        A quick correlation analysis in Pandas.

Customization

    Feel free to modify the dataset in create_and_populate_db to reflect your own data.
    Edit the SQL queries or add new queries to showcase additional SQL proficiency (joins, subqueries, etc.).
    If you want to persist the data, replace ":memory:" with a file path (e.g., "climate_demo.db").

License

Distributed for demonstration purposes under the MIT License. Feel free to use or adapt it for your own projects!
