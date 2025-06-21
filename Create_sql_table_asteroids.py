import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "Shruti@12",
    database = "nasa")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS asteroids (
    id INT,
    name VARCHAR(500),
    absolute_magnitude_h FLOAT,
    estimated_diameter_min_km FLOAT,
    estimated_diameter_max_km FLOAT,
    is_potentially_hazardous_asteroid BOOLEAN
)
""")
connection.commit()
connection.close()