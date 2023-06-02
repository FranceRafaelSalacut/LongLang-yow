import sqlite3
import requests

# Connect to the database
conn = sqlite3.connect('Final_jeep.db')
cursor = conn.cursor()

# Add latitude and longitude columns to the existing table
cursor.execute("ALTER TABLE Jeepney ADD COLUMN latitude REAL")
cursor.execute("ALTER TABLE Jeepney ADD COLUMN longitude REAL")

# Execute the SQL query to get unique locations
cursor.execute("SELECT DISTINCT location FROM Jeepney ORDER BY location")

# Fetch all the unique results
results = cursor.fetchall()

# Geocoding API endpoint
geocoding_endpoint = "https://maps.googleapis.com/maps/api/geocode/json"

# API key
api_key = "AIzaSyDljg5Fe3T6V3iieR6fCIKQS12M-iTg68o"

# Update the latitude and longitude columns in the database
for row in results:
    location = row[0]
    print(location)
    print()
    try:
        # Make a request to the Geocoding API
        response = requests.get(geocoding_endpoint, params={"address": location + ", Cebu Island, Philippines", "key": api_key})
        data = response.json()
        # Parse the response to get the latitude and longitude
        if data['status'] == 'OK':
            coordinates = data['results'][0]['geometry']['location']
            latitude = coordinates['lat']
            longitude = coordinates['lng']
            cursor.execute("UPDATE Jeepney SET latitude = ?, longitude = ? WHERE location = ?", (latitude, longitude, location))
        else:
            print(f"Coordinates not found for location: {location}")
    except Exception as e:
        print(f"Error occurred for location: {location} - {str(e)}")

# Commit the changes and close the database connection
conn.commit()
conn.close()