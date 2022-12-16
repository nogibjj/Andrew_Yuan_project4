'''
1. This python file is going to create a database and a covid_cases table
2. Load the data from csv into the table
'''

import sqlite3
import csv

# connect to the sqlite database
conn = sqlite3.connect(database = "covid.db")
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists
cursor.execute("DROP TABLE IF EXISTS covidCases")
print("Table dropped... ")

# create a table
cursor.execute(
    """
    CREATE TABLE covidCases(
        Country TEXT,
        Region TEXT,
        Total_Cases INTEGER,
        Total_Deaths INTEGER
    )          
    """
    )
print("covidCases table is created")

# create a insertion command 
cmd = "INSERT INTO covidCases (Country, Region, Total_Cases, Total_Deaths) Values (?,?,?,?)"


with open("covid_19_cases.csv","r") as read_obj:
    csv_reader = csv.reader(read_obj)
    header = next(csv_reader)
    if header != None:
        for row in csv_reader:
            cursor.execute(cmd,(row[0],row[1],row[2],row[7]))

conn.commit()
print("Loading table finishes")

#  print the table
cursor.execute("SELECT * FROM covidCases")
print(cursor.fetchall())

conn.close()

        