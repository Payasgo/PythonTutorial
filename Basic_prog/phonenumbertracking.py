import phonenumbers
from phonenumbers import carrier


number = "+917386979222"

parsed_number = phonenumbers.parse(number)

carrier_name = carrier.name_for_number(parsed_number, "en")

print(carrier_name)




'''def track_phone_number(phone_number):
    try:
        number = phonenumbers.parse(phone_number)
        if phonenumbers.is_valid_number(number):
            region = phonenumbers.region_code_for_number(number)
            carrier = phonenumbers.carrier.name_for_number(number)
            print("phone number is vaild.")
            print("Region: ", region)
            print("carrier: ", carrier)
        else:
            print("Invalid phone number.")
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Error parsing phone number.")
    
#Example usage
track_phone_number("+917386979222")'''