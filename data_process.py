import sqlite3


# three options to choose

# choice 1 : fetch the data of one country
cmd1 = """
    SELECT * FROM covidCases 
    WHERE Country ==?
"""

# choice 2 : sort the countries by either total_cases
cmd2 = """
    SELECT Country FROM covidCases 
    ORDER BY Total_Cases DESC

"""


# choice 3: alter the table to have a new column which is the ratio of death-infection
# sort countires by this new column and return 
cmd3 = """
    ALTER TABLE covidCases
    ADD COLUMN Death_Infection 'float';
    UPDATE covidCases SET Death_Infection = Total_Deaths/Total_Cases
"""


def main(choice,name):
    conn = sqlite3.connect("covid.db")
    cursor = conn.cursor()
    if choice == 1:
        print("You choose choice 1 to fetch country data")
        cursor.execute(cmd1,(name,))
        result = cursor.fetchall()
        print(result)
        pass
    elif choice == 2:
        print("You choose choice 2 to sort the countries by total cases")
        cursor.execute(cmd2)
        result = cursor.fetchmany(size=25)
        print(result)
        pass
    elif choice ==3:
        print("You choose choice 3 to sort the countries by ratio of death to infection")
        cursor.executescript(cmd3)
        conn.commit()
        # countries,total_cases,total_deaths= [row[0],row[2],row[3] for row in cursor.execute("SELECT * FROM covidCases")]
        # count =0
        # for c in countries:
        #     cursor.execute("UPDATE MyTable SET Death_Infection = ? WHERE Country = ?",
        #                 [total_cases[count]/total_deaths[count], c])
        cursor.execute('SELECT Country FROM covidCases ORDER BY Death_Infection DESC')
        result = cursor.fetchmany(size=25)
        print(result)
        pass
    else:
        print('wrong command option')
        exit()
        pass

if __name__ == '__main__':
    print("++++++++++")
    main()