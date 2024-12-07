import mysql.connector
import numpy as np

# Connect to the database
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='your_username',
    password='your_password',
    database='db_kelompok3'
)
cursor = conn.cursor()

# Retrieve data
cursor.execute("SELECT id, distance_x_cm, distance_y_cm FROM data")
points = cursor.fetchall()

# Close the database connection
cursor.close()
conn.close()

# Convert data to a list of tuples with floats
coordinates = [(float(row[1]), float(row[2])) for row in points]

