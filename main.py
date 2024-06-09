import requests
import hashlib
import time
import json

# Facebook Pixel ID and Access Token
PIXEL_ID = 'YOUR_PIXEL_ID'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

# Function to hash user data
def hash_data(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Function to send conversion event
def send_conversion_event(email, phone): 
    url = f"https://graph.facebook.com/v14.0/{PIXEL_ID}/events"
    headers = {
        "Content-Type": "application/json"
    }
    
    user_data = {
        "em": hash_data(email),
        "ph": hash_data(phone)
    }
    
    event_data = {
        "data": [
            {
                "event_name": "Purchase",
                "event_time": int(time.time()),
                "action_source": "website",
                "user_data": user_data
            }
        ]
    }
    
    params = {
        "access_token": ACCESS_TOKEN
    }
    
    response = requests.post(url, headers=headers, params=params, data=json.dumps(event_data))
    
    if response.status_code == 200:
        print("Event sent successfully")
    else:
        print(f"Failed to send event: {response.status_code} - {response.text}")

# Usage example
email = 'user@example.com'
phone = '1234567890'
send_conversion_event(email, phone)
