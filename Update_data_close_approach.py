import mysql.connector
from Asteroidsdata import asteroids_data

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "Shruti@12",
    database = "nasa")
cursor = connection.cursor()
for i in asteroids_data:
    cursor.execute("""INSERT into close_approach(
        neo_reference_id,
        close_approach_date,
        relative_velocity_kmph,
        astronomical,
        miss_distance_km,
        miss_distance_lunar,
        orbiting_body)
        values(%s, %s, %s, %s, %s, %s, %s)""",
                (i['neo_reference_id'],
    i['close_approach_date'],
    i['relative_velocity_kmph'],
    i['astronomical'],
    i['miss_distance_km'],
    i['miss_distance_lunar'],
    i['orbiting_body'])
        )
connection.commit()
connection.close()