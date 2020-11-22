import requests, json
import pandas as pd
# Enter your API key here
api_key = "804900cddabddb2ff1781dd4a29ab63d"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#http://api.openweathermap.org/data/2.5/weather?appid=804900cddabddb2ff1781dd4a29ab63d&q=mumbai
#http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&appid=804900cddabddb2ff1781dd4a29ab63d
# Give city name
city_name = input("Enter city name : ")

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

    # store the value of "main"
    # key in variable y
    y = x["main"]

    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]

    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding
    # to the "humidity" key of y
    current_humidiy = y["humidity"]

    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    # print following values
    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidiy) +
          "\n description = " +
          str(weather_description))
    table = {'Title':['Temperature','Atmospheric Pressure','Humidity','Description','City'],'value':[str(current_temperature),str(current_pressure),str(current_humidiy),str(weather_description),str(city_name)]}
    df = pd.DataFrame(table,columns=['Title','value'])
    print (df)
    df.to_csv('table.csv',index=True)

else:
    print(" City Not Found ")