# Forecast and Weather Apps
These are two different GUIs created in python to either display the current weather or a 3 hour / 5 day forecast of any village, town or city. The weather data is taken directly from a Weather API, this program processes this data and displays it in a way that is easy to understand.
## Prerequisites
Must have Python with the following modules downloaded: tkinter, requests, json, datetime and PIL.

Must also have all images downloaded in the same file as the forecast and weather apps.
## Functionality

The screen displayed when the Weather App is launched:

![WeatherAppTest1](https://github.com/user-attachments/assets/7d98d95a-a9b8-4416-8c9c-946e1343d5db)

As seen above, once the program is launched the current day, date and time is displayed at the top.
I have tailored 2 shortcut buttons, 'Home' and 'Uni', for personal use.
There is also a logo at the bottom that I created myself.

Most area is initially blank space, once a location is searched using the search bar then the screen displayed is as below:

![WeatherAppTest2](https://github.com/user-attachments/assets/3792b7d7-9ee0-49da-be89-29cead30cb06)

The app displays the current temperature, amount of rain forecast for the hour, weather description and an icon I created myself to reflect the current weather. The location is also displayed underneath the search bar along with the country code.
If an invalid location is searched then an error message is displayed.

There is an advanced information checkbox that when selected upon searching will display extra information as seen below:

![WeatherAppTest3](https://github.com/user-attachments/assets/3dc025be-12ce-4852-a80d-3c228c5ed57c)

The screen displayed when the Forecast App is launched:

![ForecastAppTest1](https://github.com/user-attachments/assets/c078aa82-24e6-4252-b5a5-bf0bd21a7db5)

It is similar to the Weather App showing the current day, date and time upon launch with a search bar and two shorcut buttons underneath.

When the 'Uni' button is clicked and the current date is selected, the following screen displayed is:

![ForecastAppTest2](https://github.com/user-attachments/assets/8993178d-b23e-4c57-a4fd-a19a9fd78d40)

The screen displays the projected weather forecast for the searched location, this includes the starting time, temperature, description, rainfall and an icon. In this instance the location is Coventry which is the intended location of the 'Uni' shortcut button. Depending on the time of day in which the forecast is searched, the amount of rows of forecast data displayed will vary.

When a new location and date is searched, this screen is displayed:

![ForecastAppTest3](https://github.com/user-attachments/assets/7241eeae-ace5-4c39-92fb-cbdedab75ceb)

This shows a whole day forecast of weather including a specific amount of projected rainfall over a 3 hour period.

If an invalid location is searched then the following screen is displayed:

![ForecastAppTest4](https://github.com/user-attachments/assets/10879cf9-5e98-47ae-a436-09d18a18ca1d)

This is similar to the Weather App where a red error message appears under the search bar.

## Project Details
This project taught me a lot about how to create efficient Python GUIs as well as improving my data collection and analysing skills. I also improved my graphic design skills as I created the logo and all of the icons.

Both programs fulfill their purposes as accurate, easy-to-use weather apps.
