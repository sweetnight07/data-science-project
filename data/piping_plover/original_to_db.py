import sqlite3

# Create a SQLite database connection
conn = sqlite3.connect('observations.db')

# Create a cursor object to execute SQL queries
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS "Observations";')

# Create a table to store the observations
cur.execute('''CREATE TABLE IF NOT EXISTS Observations (
                Common_Name TEXT,
                Scientific_Name TEXT,
                Observation_Count INTEGER,
                county_name TEXT,
                Latitude REAL,
                Longitude REAL,
                Observation_Date TEXT
            )''')

# Open the original file for reading
with open('piping_plover_data/ebd_US_pipplo_relFeb-2024.txt', 'r', encoding='utf-8') as infile:
    # Iterate through each line in the original file
    for line in infile:
        # Split the line based on tab ('\t') delimiter
        rows = line.strip().split('\t')
      
        # Insert the row into the database
        cur.execute("INSERT INTO Observations (Common_Name, Scientific_Name, Observation_Count, county_name, Latitude, Longitude, Observation_Date) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (rows[5], rows[6], rows[10], rows[19], rows[28], rows[29], rows[30]))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database created successfully.")