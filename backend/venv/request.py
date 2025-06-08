import requests

#url 
url = 'http://127.0.0.1:5000/predict_api'
#data to be sent to api

data = {
    'City': 'Bangalore',
    'BHK': 2,
    'Size': 1200,
    'Floor': 5,
    'AreaType': 'Super built-up',
    'FurnishingStatus': 'Semi-furnished',
    'Bathroom': 2
}

#sending post request and saving response as response object
response = requests.post(url, json=data)

# extracting data in json format
prediction = response.json()
print(prediction)