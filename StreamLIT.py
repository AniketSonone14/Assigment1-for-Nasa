import streamlit as st
from datetime import datetime
import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "Shruti@12",
    database = "nasa")
cursor = connection.cursor()
st.markdown("""
<h3 
            style='text-align: center; color: #5dade2; font-weight:bold; font-size:28px;
           font-family:Trebuchet MS; text-shadow: 1px 1px 2px black;'>
🔭 NASA Near-Earth Object (NEO) Tracking & Insights            
</h3>
""", unsafe_allow_html=True)
st.sidebar.markdown(
    "<span style='color:#FF4B4B; font-weight:bold; font-size:25px;'>🎯 Asteroid <br>    Approaches</span>",
    unsafe_allow_html=True
)
tab=st.sidebar.radio("-------------------", ["Filter", "Queries"])
if tab == "Queries":
    st.sidebar.title("NEO Query Explorer")
    query_options = [
    "Count how many times each asteroid has approached Earth",
    "Average velocity of each asteroid over multiple approaches",
    "List top 10 fastest asteroids",
    "Find potentially hazardous asteroids that have approached Earth more than 3 times",
    "Find the month with the most asteroid approaches",
    "Get the asteroid with the fastest ever approach speed",
    "Sort asteroids by maximum estimated diameter (descending)",
    "An asteroid whose closest approach is getting nearer over time", 
    "Display the name of each asteroid along with the date and miss distance of its closest approach to Earth",
    "List names of asteroids that approached Earth with velocity > 50,000 km/h",
    "Count how many approaches happened per month",
    "Find asteroid with the highest brightness (lowest magnitude value)",
    "Get number of hazardous vs non-hazardous asteroids",
    "Find asteroids that passed closer than the Moon (lesser than 1 LD), along with their close approach date and distance",
    "Find asteroids that came within 0.05 AU(astronomical distance)",
    "Top 5 Closest Approaches in Terms of Distance (km)",
    "Most Active Asteroids (Top 5 by Approach Frequency)",
    "Yearly Hazardous Asteroid Count",
    "Top 5 Brightest Asteroids",
    "Asteroids with Large Size Range"]
    selected_query = st.selectbox("Select a Query", query_options)
    if selected_query == "Count how many times each asteroid has approached Earth":
      cursor.execute('''SELECT  name, COUNT(*) AS approach_count
                     FROM asteroids GROUP BY name
                     ORDER BY approach_count''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results,columns=columns)
      st.dataframe(data)
    elif selected_query ==  "Average velocity of each asteroid over multiple approaches":
      cursor.execute('''SELECT a.name, c.neo_reference_id, AVG(c.relative_velocity_kmph) AS average_velocity
                    FROM asteroids AS a JOIN close_approach AS c 
                    ON a.id = c.neo_reference_id
                    GROUP BY c.neo_reference_id, a.name''') 
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results,columns=columns)
      st.dataframe(data)
    elif selected_query == "List top 10 fastest asteroids":
      cursor.execute('''SELECT a.name FROM asteroids AS a
                     JOIN close_approach AS c 
                     ON a.id = c.neo_reference_id
                     order by c.relative_velocity_kmph desc limit 10''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Find potentially hazardous asteroids that have approached Earth more than 3 times":
      cursor.execute('''SELECT name, COUNT(*) AS approach_count
                        FROM asteroids GROUP BY name
                        HAVING COUNT(*) > 3 ORDER BY approach_count DESC''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Find the month with the most asteroid approaches":
      cursor.execute('''SELECT MONTH(close_approach_date) AS approach_month,		
                        COUNT(*) AS total_approaches FROM close_approach		
                        GROUP BY MONTH(close_approach_date)		
                        ORDER BY total_approaches DESC	LIMIT 1''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Get the asteroid with the fastest ever approach speed":
      cursor.execute('''SELECT a.name, c.relative_velocity_kmph
                        FROM asteroids AS a JOIN close_approach AS c 
                        ON a.id = c.neo_reference_id
                        ORDER BY c.relative_velocity_kmph DESC
                        LIMIT 1''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Sort asteroids by maximum estimated diameter (descending)":
      cursor.execute('''Select 	name,estimated_diameter_max_km
                        from asteroids order by	estimated_diameter_max_km desc''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "An asteroid whose closest approach is getting nearer over time":
      cursor.execute('''SELECT a.name,c.close_approach_date,c.miss_distance_km
                        FROM asteroids AS a JOIN  close_approach AS c 
                        ON a.id = c.neo_reference_id
                        ORDER BY a.name,c.close_approach_date ASC''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Display the name of each asteroid along with the date and miss distance of its closest approach to Earth":
      cursor.execute('''SELECT a.name, c.close_approach_date, c.miss_distance_km
                        FROM asteroids AS a JOIN  close_approach AS c 
                        ON a.id = c.neo_reference_id
                        ORDER BY  c.miss_distance_km ASC''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)   
    elif selected_query == "List names of asteroids that approached Earth with velocity > 50,000 km/h":
      cursor.execute('''Select	a.name, c.relative_velocity_kmph
                     	From asteroids as a Join close_approach as c
                        on 	a.id = c.neo_reference_id	
                        where	relative_velocity_kmph > 50000''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Count how many approaches happened per month":
      cursor.execute('''SELECT MONTH(close_approach_date) AS approach_month,		
                        COUNT(*) AS total_approaches FROM close_approach		
                        GROUP BY MONTH(close_approach_date)''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Find asteroid with the highest brightness (lowest magnitude value)":
      cursor.execute('''Select name ,absolute_magnitude_h
                        from Asteroids
                        order by absolute_magnitude_h asc limit 1''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Get number of hazardous vs non-hazardous asteroids":
      cursor.execute('''select 	is_potentially_hazardous_asteroid, count(*) as hardous_count	
                        from  Asteroids	group by is_potentially_hazardous_asteroid''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Find asteroids that passed closer than the Moon (lesser than 1 LD), along with their close approach date and distance":
      cursor.execute('''SELECT a.name, c.close_approach_date, c.miss_distance_lunar
                        FROM asteroids AS a JOIN close_approach AS c 
                        ON a.id = c.neo_reference_id
                        WHERE c.miss_distance_lunar < 1 ORDER BY c.miss_distance_lunar ASC''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Find asteroids that came within 0.05 AU(astronomical distance)":
      cursor.execute('''Select	a.name,	c.astronomical
                        from Asteroids as a join close_approach as c
                        on a.id = c.neo_reference_id	
                        where astronomical<= 0.05 order by astronomical''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Top 5 Closest Approaches in Terms of Distance (km)":
      cursor.execute('''SELECT a.name,c.close_approach_date,c.miss_distance_km
                        FROM asteroids AS a JOIN close_approach AS c 
                        ON a.id = c.neo_reference_id
                        ORDER BY c.miss_distance_km ASC LIMIT 5''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Most Active Asteroids (Top 5 by Approach Frequency)":
      cursor.execute('''SELECT a.name, COUNT(*) AS total_approaches
                        FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id
                        GROUP BY a.name
                        ORDER BY total_approaches DESC LIMIT 5''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Yearly Hazardous Asteroid Count":
      cursor.execute('''SELECT YEAR(c.close_approach_date) AS year, COUNT(*) AS hazardous_count
                        FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id
                        WHERE a.is_potentially_hazardous_asteroid = TRUE
                        GROUP BY year ORDER BY year''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Top 5 Brightest Asteroids":
      cursor.execute('''SELECT name,absolute_magnitude_h
                        FROM asteroids
                        ORDER BY absolute_magnitude_h ASC LIMIT 5''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)
    elif selected_query == "Asteroids with Large Size Range":
      cursor.execute('''SELECT name,   estimated_diameter_max_km - estimated_diameter_min_km AS diameter_range
                        FROM asteroids
                        ORDER BY diameter_range DESC''')
      results = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      data = pd.DataFrame(results, columns=columns)
      st.dataframe(data)                                  
else :
  st.sidebar.markdown("### 🛠️ **Customize Your Filters**")
  st.sidebar.markdown("---")
  col1, col2, col3 = st.columns(3)
  with col1:
   st.markdown("###### 📅 Date Range")
   start_date = st.date_input("Start Date", datetime(2024, 1, 1))
   end_date = st.date_input("End Date", datetime(2024, 12, 31))
  with col2: 
   st.markdown("###### 🌌 Distance Filters")
   au = st.slider("Astronomical Units (AU)", 0.0, 1.0, (0.0, 1.0))
   ld = st.slider("Lunar Distances (LD)", 0.0, 300.0, (0.0, 300.0))
  with col3: 
   st.markdown("###### 🚀 Velocity & Size")
   velocity = st.slider("Relative Velocity (km/h)", 0.0, 150000.0, (0.0, 150000.0))
   diameter_min = st.slider("Estimated Diameter Min (km)", 0.0, 2.0, (0.0, 2.0))
   diameter_max = st.slider("Estimated Diameter Max (km)", 0.0, 5.0, (0.0, 5.0))
  st.markdown("###### ☄️ Hazard Risk")
  hazardous = st.selectbox("Is Hazardous?", ["All", "True", "False"])
  st.markdown("---")
  st.sidebar.markdown("🛰️ *Refine your filters to explore the asteroid data more effectively.*")
  base_query ='''SELECT 
    a.name,
    c.close_approach_date,
    c.relative_velocity_kmph,
    c.astronomical,
    c.miss_distance_lunar,
    c.miss_distance_km,
    a.estimated_diameter_min_km,
    a.estimated_diameter_max_km,
    a.is_potentially_hazardous_asteroid
    FROM 
    asteroids AS a
    JOIN 
    close_approach AS c 
    ON 
    a.id = c.neo_reference_id
    WHERE 
    c.close_approach_date BETWEEN %s AND %s  
    AND c.astronomical BETWEEN %s AND %s
    AND c.miss_distance_lunar BETWEEN %s AND %s
    AND c.relative_velocity_kmph BETWEEN %s AND %s
    AND a.estimated_diameter_min_km BETWEEN %s AND %s
    AND a.estimated_diameter_max_km BETWEEN %s AND %s
    ''' 
  Paras = [start_date,end_date,
         au[0],au[1],
         ld[0], ld[1],
         velocity[0], velocity[1],
         diameter_min[0],diameter_min[1],
         diameter_max[0],diameter_max[1]]
  if hazardous != "All":
    base_query += " AND a.is_potentially_hazardous_asteroid = %s"
    Paras.append(hazardous == "True")
  cursor.execute(base_query, Paras)
  rows = cursor.fetchall()
  columns = [desc[0] for desc in cursor.description]
  df = pd.DataFrame(rows, columns=columns)
  st.dataframe(df)
cursor.close()
connection.close()