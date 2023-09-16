import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

import folium

from opencage.geocoder import OpenCageGeocode

# Taking input the phonenumber along with the country code
number = input("Enter the phonenumber with the country code :")

#parsing string to the phonenumbrt
phoneNumber = phonenumbers.parse(number,'IN')

# Storing the APU key in the key variable
key = "b8817ed6604c4970850e644f9682e641"

# printing the gelocation of thr given number using the geocoder module
geolocation = geocoder.description_for_number(phoneNumber,"en")
print("location : "+geolocation)

#printing the service provider name using the carrier module
service = carrier.name_for_number(phoneNumber,"en")
print("service :"+service)

# Using opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(key)
addressfile = 'addresses.txt'
query = str("yourLocation")
results = geocoder.geocode(query, no_annotations = '1')

# Assigning the latitude and longtitude values to the lat and lng variables
if results and len(results):
    longitude = results[0]['geometry']['lng']
    latitude = results[0]['geometry']['lat']
    print(u'%f;%f;%s;%s' % (results[0]['geometry']['lng'],
                        results[0]['geometry']['lat'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))

# Getting the map for the given latitude and longitude
myMap = folium.Map(location=['lng','lat'],zoom_start = 9)

# Adding a Marker on the mao to show the location name
folium.Marker([location["Longitude"],'lat'],popup='yourLocation').add_to(myMap)

# Save the map to an HTML file to open it and see the actual location in map format
myMap.save("Location.html")