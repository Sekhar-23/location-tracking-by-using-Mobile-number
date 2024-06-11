import requests
import json

def get_location_by_phone(phone_number):
    try:
        url = f"https://www.freecarrierlookup.com/reversephonelookup?number={phone_number}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        if data.get("status") == "OK":
            location = data["carrier"]["location"]
            return location
        else:
            print("Error: Unable to retrieve location information.")
            return None
    except requests.exceptions.RequestException as e:
        print("Error: Failed to make the request:", e)
        return None
    except json.JSONDecodeError as e:
        print("Error: Failed to decode JSON response:", e)
        return None

phone_number = "7569995773"
location = get_location_by_phone(phone_number)
print(location)
