import requests

def get_weather(city, api_key):
    """
    Fetch the weather data from OpenWeatherMap API for the given city.
    """
    # Define the URL and parameters for the API request
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Make the GET request to the API
    response = requests.get(url)
    
    # If the response is successful (status code 200), return the weather data
    if response.status_code == 200:
        return response.json()  # Parse the JSON data
    else:
        return None  # Return None if city is not found or there is an error

def display_weather(data):
    """
    Display the weather data to the user.
    """
    if data:
        # Extract useful information from the data
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        
        # Display the weather information
        print(f"Weather: {weather}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
    else:
        # If no data was found, print an error message
        print("City not found! Please check the city name or try again.")

def main():
    """
    Main function to run the weather forecasting app.
    """
    # Prompt the user to enter the city name
    city = input("Enter the city name: ")
    
    # Replace with your OpenWeatherMap API key
    api_key = "34ca55ca3c941d00a4a1d02f2a4450e7"
    
    # Fetch the weather data for the entered city
    weather_data = get_weather(city, api_key)
    
    # Display the fetched weather data
    display_weather(weather_data)

if __name__ == "__main__":
    main()
