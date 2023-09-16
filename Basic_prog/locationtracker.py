from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

geolocator = Nominatim(user_agent="location_tracker")

def get_location(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except GeocoderTimedOut:
        return None

# Example usage
address = "1600 Amphitheatre Parkway, Mountain View, CA"
location = get_location(address)
if location:
    print("Latitude:", location[0])
    print("Longitude:", location[1])
else:
    print("Could not find location for address:", address)