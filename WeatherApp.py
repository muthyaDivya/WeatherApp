
# ! Welcome Message

print("\nWelcome to the Weather App!\n")

# ! Hardcoded weather data

weather_data = {"London" :{"temperature": "15 deg", "condition": "Cloudy", "wind_speed":"15km/hr", "humidity": "80%"},
                "New York":{"temperature": "20 deg", "condition":"Sunny", "wind_speed":"5km/hr", "humidity":"30%"},
                "Berlin":{"temperature": "12 deg", "condition":"Cloudy", "wind_speed":"12km/hr", "humidity":"70%"},
                "Paris":{"temperature": "13 deg", "condition":"Foggy", "wind_speed":"5km/hr", "humidity":"90%"},
                "Rome":{"temperature": "10 deg", "condition":"Cloudy", "wind_speed":"8km/hr", "humidity":"75%"},
                "Sydney":{"temperature": "22 deg", "condition":"Sunny", "wind_speed":"4km/hr", "humidity":"45%"},
                "Tokyo":{"temperature": "16 deg", "condition":"Partly Cloudy", "wind_speed":"6km/hr", "humidity":"60%"},
                "Bangalore":{"temperature": "18 deg", "condition":"Sunny", "wind_speed":"8km.hr", "humidity":"40%"},
                "New Delhi":{"temperature": "32 deg", "condition":"Sunny", "wind_speed":"6km/hr", "humidity":"45%"},
                "Shanghai":{"temperature": "18 deg", "condition":"Rainy", "wind_speed":"3km/hr", "humidity":"50%"},
                "Mumbai":{"temperature": "29 deg", "condition":"Rainy", "wind_speed":"5km/hr", "humidity":"50%"},
                "Barcelona":{"temperature": "22 deg", "condition":"Sunny", "wind_speed":"2km/hr", "humidity":"30%"},
                "Geneva":{"temperature": "13 deg", "condition":"Cloudy", "wind_speed":"4km/hr", "humidity":"67%"},
                "Amsterdam":{"temperature": "12 deg", "condition":"Rainy", "wind_speed":"5km/hr", "humidity":"84%"},
                "Brussels":{"temperature": "14 deg", "condition":"Foggy", "wind_speed":"8km/hr", "humidity":"93%"}
                }

# ! User input

city_of_choice = input("Select a city:")


# ! Function to Fetch and display the data of a city 
def data_fetch(city_chosen):
        # Convert dictionary items to a list and initialize an index for the while loop
        items = list(weather_data.items())
        index = 0
        try:
            # Use a while loop to iterate through the dictionary
            while index < len(items):
                city, data = items[index]
                # Convert both to lowercase for comparison
                if city.lower() == city_chosen.lower():  
                    print(f"\n{city} Weather Today:\n")
                    print(f"Current Temperature: {data['temperature']}")
                    print(f"Condition: {data['condition']}")
                    print(f"Wind_Speed: {data['wind_speed']}")
                    print(f"Humidity: {data['humidity']}")
                    break # Exit the loop once city is found

                index += 1  # Move to the next item in the dictionary
            else:
                raise KeyError("Unknown City")
            
        except KeyError as e:
            print(f"KeyError: {e}")
            
        finally:
            print("\n Thank you for choosing the Weather App!\n")

# ! check if user entered a 'digit/ kept empty' instead of city name
if not city_of_choice:
    print("City name cannot be empty. Please enter a valid city name!")
elif city_of_choice.isdigit():
    print("City name cannot be a digit. Please enter a valid city name")
else:
    data_fetch(city_of_choice)













# def data_fetch(city_chosen):
#         try:
#             for city,data in weather_data.items():
#                 if city.lower() == city_chosen.lower():
#                     print(f"\n{city} Weather Today:\n")
#                     print(f"Current Temperature: {weather_data[city]["temperature"]}")
#                     print(f"Condition: {weather_data[city]["condition"]}")
#                     print(f"Wind_Speed: {weather_data[city]["wind_speed"]}")
#                     print(f"Humidity: {weather_data[city]["humidity"]}")
#                     break
#                 else:
#                     raise KeyError("Unknown City")
#         except KeyError as e:
#             print(f"KeyError: {e}")
#         finally:
#             print("\n Thank you for choosing the Weather App!\n")


# data_fetch(city_of_choice)