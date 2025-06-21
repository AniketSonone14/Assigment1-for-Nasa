import mysql.connector
from Asteroidsdata import asteroids_data

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "Shruti@12",
    database = "nasa")
cursor = connection.cursor()
for i in asteroids_data:
    cursor.execute("""INSERT into asteroids (id, 
        name, 
        absolute_magnitude_h, 
        estimated_diameter_min_km, 
        estimated_diameter_max_km, 
        is_potentially_hazardous_asteroid)
        values(%s, %s, %s, %s, %s, %s)""",
                (i['id'],
    i['name'],
    i['absolute_magnitude_h'],
    i['estimated_diameter_min_km'],
    i['estimated_diameter_max_km'],
    i['is_potentially_hazardous_asteroid'])
        )
connection.commit()
connection.close()