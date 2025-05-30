# FastAPI SQL Server Example

This project demonstrates how to build a simple **FastAPI** application that connects to a SQL Server database using `pyodbc` and exposes an endpoint to fetch all rows from a table.

---

## Features

- Connects to SQL Server using `pyodbc`
- Exposes a REST API endpoint (`/asd`) to fetch all rows from the `asD` table
- Returns results as JSON

---

## Prerequisites

- Python 3.7+
- SQL Server (local or remote)
- [ODBC Driver for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server) (e.g., ODBC Driver 17 for SQL Server)
- Python packages: `fastapi`, `uvicorn`, `pyodbc`

---

## Installation

1. **Install Python dependencies:**
    ```
    pip install fastapi uvicorn pyodbc
    ```

2. **Install the ODBC Driver for SQL Server:**
    - [Download from Microsoft](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)
    - Make sure the driver name matches what you use in your connection string (see below).

---

## Usage

1. **Update the database connection details in your Python script:**

    ```python
    def get_connection():
        conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"
            "DATABASE=YourDatabaseName;"
            "UID=YourUsername;"
            "PWD=YourPassword;"
        )
        return pyodbc.connect(conn_str)
    ```
    - Replace `ODBC Driver 17 for SQL Server` with your installed driver (check with `pyodbc.drivers()`).
    - Replace `YourDatabaseName`, `YourUsername`, and `YourPassword` with your actual credentials.

2. **Ensure your table exists:**

    ```sql
    CREATE TABLE asD (
        id INT PRIMARY KEY,
        name NVARCHAR(100),
        email NVARCHAR(100)
    );
    ```

3. **Run the FastAPI app:**
    ```
    uvicorn app:app --reload
    ```
    - `app` is the filename (without `.py`), and the second `app` is the FastAPI instance.

4. **Access the API:**
    - Open your browser or API client and go to: [http://localhost:8000/asd](http://localhost:8000/asd)
    - You can also view the interactive docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Example Endpoint

- **GET** `/asd`  
  Returns all rows from the `asD` table as a JSON array.

---

## Troubleshooting

- **ODBC Driver errors:**  
  Make sure the driver name in your connection string matches what is installed. Check with:
    ```python
    import pyodbc
    print(pyodbc.drivers())
    ```
- **404 Not Found:**  
  Make sure you are visiting the correct endpoint (`/asd`) and that the server is running.
- **500 Internal Server Error:**  
  Check your database credentials, table existence, and server status.

---

