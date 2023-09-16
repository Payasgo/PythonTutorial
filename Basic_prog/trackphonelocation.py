import requests

def track_phone_number(phone_number):
    api_key = "b8817ed6604c4970850e644f9682e641"  # Replace with your NumVerify API key
    url = f"https://api.opencagedata.com/geocode/v1/json?q=URI-ENCODED-PLACENAME&key=b8817ed6604c4970850e644f9682e641&number={phone_number}"
    
    response = requests.get(url)
    data = response.json()
    
    if data["valid"]:
        print("Phone number is valid")
        print("Country:", data["country_name"])
        print("Location:", data["location"])
        print("Carrier:", data["carrier"])
    else:
        print("Invalid phone number")
        
# Example usage
phone_number = "+917386979222"  # Replace with the phone number you want to track
track_phone_number(phone_number)