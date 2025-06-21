import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "Shruti@12",
    database = "nasa")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS close_approach (
    neo_reference_id INT,
    close_approach_date DATE,
    relative_velocity_kmph FLOAT,
    astronomical FLOAT,
    miss_distance_km FLOAT,
    miss_distance_lunar FLOAT,
    orbiting_body VARCHAR(50)
)
""")
connection.commit()
connection.close()