from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.get("/")
async def root():
    return {"Welcome to the covid-19 cases searching microservice"}

@app.get("/countries/{country_name}")
async def fetch_item(country_name):
    conn = sqlite3.connect("covid.db")
    cursor = conn.cursor()
    cmd1 = """
        SELECT * FROM covidCases 
        WHERE Country ==?
    """
    cursor.execute(cmd1,(country_name,))
    result = cursor.fetchall()
    return result

@app.get("/sort")
async def sort_by_total_cases():
    conn = sqlite3.connect("covid.db")
    cursor = conn.cursor()
    cmd2 = """
    SELECT Country FROM covidCases 
    ORDER BY Total_Cases DESC

    """
    cursor.execute(cmd2)
    result = cursor.fetchmany(size=25)
    return result 



    


    
