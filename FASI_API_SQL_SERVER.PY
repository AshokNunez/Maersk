from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
import pyodbc

app = FastAPI()

def get_connection():
    conn_str = (
        "DRIVER={SQL SERVER};"
        "SERVER=localhost;"
        "DATABASE=YourDatabaseName;"
        "UID=YourUsername;"
        "PWD=YourPassword;"
    )
    return pyodbc.connect(conn_str)

@app.get("/asd", response_model=List[Dict[str, Any]])
def read_asd():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM asD;")
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
