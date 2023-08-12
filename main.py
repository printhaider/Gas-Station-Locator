import googlemaps

# Get user input for the API key
api_key = input("Enter your Google Maps API key: ")

# Initialize the Google Maps client with the user-provided API key
gmaps = googlemaps.Client(key=api_key)

# Define the location to search for gas stations
location = gmaps.geocode('100 featherstone ave, Markham, ON')[0]['geometry']['location']

# Define the search parameters
params = {
    'location': location,
    'radius': 5000,
    'type': 'gas_station',
}

# Send the request to the Places API and get the response
places_result = gmaps.places(**params)

# Create a method to output the results
def output_results(place_details):
    gas_price = place_details['result']['price_level']
    print(place_details['result']['name'], place_details['result']['vicinity'],place_details['result']['price_level'])
    print('Gas Price: ', gas_price)

# Loop through the gas stations and print their details
for place in places_result['results']:
    place_details = gmaps.place(place['place_id'], fields=['name', 'vicinity', 'price_level'])
    print('{.2f}'.format(place_details['price_level']))
