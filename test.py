from geopy.geocoders import Nominatim

# Create a geocoder instance
geolocator = Nominatim(user_agent="my_geocoder")

# Write the locations and coordinates to a text file
with open('location_coordinates.txt', 'w') as file:
        try:
            location = 'Leon Kilat St'
            # Geocode the location
            location_info = geolocator.geocode(location)
            if location_info:
                latitude = location_info.latitude
                longitude = location_info.longitude
                file.write(f"{location}: Latitude: {latitude}, Longitude: {longitude}\n")
            else:
                file.write(f"{location}: Coordinates not found\n")
        except Exception as e:
            file.write(f"{location}: Error occurred - {str(e)}\n")
