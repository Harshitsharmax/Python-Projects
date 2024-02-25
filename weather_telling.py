# Import the pyttsx3 library, which is a text-to-speech conversion library in Python.
import pyttsx3
# Import the requests library, which is used to send HTTP requests in Python.
import requests
# Import the json library, which is used to work with JSON data in Python.
import json

# Asks the user to enter the name of the city.
city = input("Enter the name of the city: ")

# Construct the URL for the weather API using the city name.
url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
# Send an HTTP GET request to the weather API.
r = requests.get(url)

# Parse the JSON response from the weather API.
wdic = json.loads(r.text)
# Extract the current temperature in Celsius from the JSON response.
w = wdic["current"]["temp_c"]

# Main logic how pyttsx3 works:
# Initialize a pyttsx3 engine.
robo = pyttsx3.init()
# Use the engine to speak the text entered by the user.
robo.say(f"The current weather in {city} is {w} degree Celsius.")
# Wait for the speech to finish.
robo.runAndWait()
