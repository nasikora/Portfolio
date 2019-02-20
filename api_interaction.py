#Python 3 API interaction file based off of:
#https://www.dataquest.io/m/52/working-with-apis/10/finding-the-number-of-people-in-space

#API data source: http://open-notify.org/Open-Notify-API/ISS-Location-Now/ 

"""
	API format:

"""
import requests
import json

try:
	# This is the latitude and longitude of San Diego lat / lon: 32.7157° N, 117.1611° W
	parameters = {"lat": 32.72, "lon": 117.16}

	# Make a get request with the parameters.
	response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

	status_code = response.status_code
	response_content = response.content 
	# Print the content of the response (the data the server returned)
	print("Status code:", status_code)

	# Get the response data as a Python object.  Verify that it's a dictionary.
	json_data = response.json()
	print(type(json_data))
	#print(json_data)

	first_pass_duration = json_data["response"][0]["duration"]

	# Headers is a dictionary
	print(response.headers)

	content_type = response.headers["content-type"]
except: 
	print("Error during execution; check prompt")


