import phonenumbers
from geopy.geocoders import Nominatim

def track_phone_number(phone_number):
    # Parse the phone number
    parsed_number = phonenumbers.parse(phone_number, None)

    # Check if the phone number is valid
    if not phonenumbers.is_valid_number(parsed_number):
        print("Invalid phone number")
        return

    # Get the country code and phone number without formatting
    country_code = phonenumbers.format_number(parsed_number.country_code, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    phone_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

    # Get the location information
    geolocator = Nominatim(user_agent="phone_number_tracker")
    location = geolocator.geocode(phone_number)

    # Print the tracking results
    print("Phone number:", phone_number)
    print("Country:", country_code)
    if location:
        print("Location:", location.address)
        print("Latitude:", location.latitude)
        print("Longitude:", location.longitude)
    else:
        print("Location information not found")

# Example usage
phone_number = ""  # Replace with the phone number you want to track
track_phone_number(phone_number)