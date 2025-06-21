from datetime import datetime
import requests

API_k = 'DCgCLtiMZ4B7CjMYhIRyBj5PcjFR6vzbQXMrduFW'

url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date=2024-01-01&end_date=2024-01-07&api_key={API_k}"

asteroids_data = []
target = 10000
while len(asteroids_data) < target:
      response = requests.get(url)
      data = response.json()
      details = data['near_earth_objects']
      for date,ast_details in details.items():
          for ast in ast_details:
            asteroids_data.append(dict(
                id = int(ast['id']),
                neo_reference_id = int(ast['neo_reference_id']),
                name = ast['name'],
                absolute_magnitude_h = float(ast['absolute_magnitude_h']),
                estimated_diameter_min_km = float(ast['estimated_diameter']['kilometers']['estimated_diameter_min']),
                estimated_diameter_max_km = float(ast['estimated_diameter']['kilometers']['estimated_diameter_max']),
                is_potentially_hazardous_asteroid = ast['is_potentially_hazardous_asteroid'],
                close_approach_date = datetime.strptime(ast['close_approach_data'][0]['close_approach_date'], "%Y-%m-%d"),
                relative_velocity_kmph = float(ast['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']),
                astronomical = float(ast['close_approach_data'][0]['miss_distance']['astronomical']),
                miss_distance_km = float(ast['close_approach_data'][0]['miss_distance']['kilometers']),
                miss_distance_lunar = float(ast['close_approach_data'][0]['miss_distance']['lunar']),
                orbiting_body = ast['close_approach_data'][0]['orbiting_body']
                ))

            if len(asteroids_data) == target:
                break
          if len(asteroids_data) == target:
                break
      url = data['links']['next']
      #print(asteroids_data[9999])