import random

# Read the location coordinates from the text file
with open('location_coordinates.txt', 'r') as file:
    locations = file.readlines()

# Shuffle the locations randomly
random.shuffle(locations)

# Select the first 10 locations
selected_locations = locations[:10]

# Print the selected locations
for location in selected_locations:
    print(location)
