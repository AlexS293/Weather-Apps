# python3 -- Weather Application using API
 
# importing the libraries
from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image
 
 
# necessary details
###### Update size
root = Tk()
root.title("Weather App") ## Create the main box pop up with specified dims.
root.geometry("600x800")
root['background'] = "White"
 
# Image
###### Get rid or create own logo w/ affinity
new = ImageTk.PhotoImage(Image.open('logo.png')) ## Add logo at the bottom
panel = Label(root, image=new)
panel.place(x=125, y=675)
 
# Dates
###### Update position
dt = datetime.datetime.now() ## Get date info
day = Label(root, text=dt.strftime('%A'), bg='white', font=("Times New Roman", 20))
day.place(x=25, y=25) ## %A gets the day, others are explanatory
date = Label(root, text=dt.strftime('%d/%m/%Y'), bg='white', font=("Times New Roman", 20))
date.place(x=200, y=25) 
 
# Time
###### Update position
hour = Label(root, text=dt.strftime('%I : %M %p'),
             bg='white', font=("Times New Roman", 20))
hour.place(x=400, y=25)
 
# Theme for the respective time the application is used
###### Can be improved to reflect current weather

 
 
# City Search
###### Update position + make larger
city_name = StringVar() ## Entry box for city/town name
city_entry = Entry(root, textvariable=city_name, width=45)
city_entry.place(x=25, y=100)

def is_on():
    if var.get() == 1:
        return True
    else:
        return False
 
def city_name(home, uni):
    api_key = 'ce8a8aed31461441ab8493097f240155'
    # API Call
    try:
        
        if home:
            api_weather_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                                   + 'Findern' + "&units=metric&appid="+api_key)
            api_forecast_request = requests.get("http://api.openweathermap.org/data/2.5/forecast?q="
                                   + 'Findern' + "&units=metric&appid="+api_key)
        elif uni:
            api_weather_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                                   + 'Coventry' + "&units=metric&appid="+api_key)
            api_forecast_request = requests.get("http://api.openweathermap.org/data/2.5/forecast?q="
                                   + 'Coventry' + "&units=metric&appid="+api_key)
        else:
            api_weather_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                                   + city_entry.get() + "&units=metric&appid="+api_key)
            api_forecast_request = requests.get("http://api.openweathermap.org/data/2.5/forecast?q="
                                   + city_entry.get() + "&units=metric&appid="+api_key)

        api_weather = json.loads(api_weather_request.content) ## Loads weather info from given city
        api_forecast = json.loads(api_forecast_request.content)
        
        # Temperatures
        y = api_weather['main']
        current_temprature = str(y['temp']) + ' °C'
        
        z = api_weather['sys']
        country = z['country']
        citi = api_weather['name']
        
        if var.get()==1 :
            humi.configure(text='Humidity: ')
            maxi.configure(text='Max Temp: ')
            mini.configure(text='Min Temp: ')
            pressure.configure(text='Pressure: ')
            wind.configure(text='Wind Speed: ')
            wind_dir.configure(text='Wind Direction: ')
            sunrise_time.configure(text='Sunrise: ')
            sunset_time.configure(text='Sunset: ')
            
            humidity = y['humidity']
            tempmin = y['temp_min']
            tempmax = y['temp_max']
            press = y['pressure']
            wind_speed = api_weather['wind']['speed']
            wind_direction = api_weather['wind']['deg']
            sunrise = z['sunrise']
            sunset = z['sunset']

            wind_directions = [0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5, 180,
                                       202.5, 225, 247.5, 270, 292.5, 315, 337.5, 360]
            wind_compass = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S',
                                    'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']
            min_sep = 360
            direction = ''
            for i in range(len(wind_directions)):
                sep = abs(wind_directions[i]-wind_direction)
                if sep<min_sep:
                    min_sep = sep
                    direction = wind_compass[i]

            sunrise_gmt = datetime.datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')
            sunrise_ltz = datetime.datetime.fromtimestamp(sunrise+api_weather['timezone']-3600).strftime('%H:%M:%S')
            sunset_gmt = datetime.datetime.fromtimestamp(sunset).strftime('%H:%M:%S')
            sunset_ltz = datetime.datetime.fromtimestamp(sunset+api_weather['timezone']-3600).strftime('%H:%M:%S')                           
            hum_str = str(humidity)+'%'
            tempmax_str = str(tempmax)+'°C'
            tempmin_str = str(tempmin)+'°C'
            press_str = str(press)+' hPa'
            windspeed_str = str(wind_speed)+' m/s'
        else:
            humi.configure(text='')
            maxi.configure(text='')
            mini.configure(text='')
            pressure.configure(text='')
            wind.configure(text='')
            wind_dir.configure(text='')
            sunrise_time.configure(text='')
            sunset_time.configure(text='')
            humidity = ''
            tempmin = ''
            tempmax = ''
            press = ''
            wind_speed = ''
            direction = ''
            sunrise_ltz = ''
            sunset_ltz = ''
            hum_str = ''
            tempmax_str = ''
            tempmin_str = ''
            press_str = ''
            windspeed_str = ''    
            

        # Rain
        try:
            rain = api_weather['rain']
            current_rain = str(rain['1h'])+' mm rain'
        except KeyError:
            current_rain = str(0) + 'mm rain'

        # Description
        weather_description = api_weather['weather']
        description = weather_description[0]['description'].title()
        text = ''
        tot = 0
        if len(description)>17:
            wordList = description.split(' ')
            for i in wordList:
                x = len(i)
                if (tot+x+1 <=17):
                    tot += x+1
                    text = text+i+' '
                else:
                    tot = x
                    text = text[:-1]
                    text = text+'\n'+i+' '      
            description = text
            
            
        # Coordinates
        x = api_weather['coord']
        longtitude = x['lon']
        latitude = x['lat']
     
        # Country
        z = api_weather['sys']
        country = z['country']
        citi = api_weather['name']
     
        # Adding the received info into the screen
        ###### Could be changed to be a multi-choice / option for more advanced info
        lable_temp.configure(text=current_temprature)
        lable_precip.configure(text=current_rain)
        lable_descr.configure(text=description)
        lable_country.configure(text=country)
        lable_citi.configure(text=citi, fg='#000')
        lable_humidity.configure(text=hum_str)
        max_temp.configure(text=tempmax_str)
        min_temp.configure(text=tempmin_str)
        lable_pressure.configure(text=press_str)
        lable_wind.configure(text=windspeed_str)
        lable_wind_dir.configure(text=direction)
        lable_sunrise.configure(text=sunrise_ltz)
        lable_sunset.configure(text=sunset_ltz)

        weather_id = int(weather_description[0]['id'])
        light_rains = [300, 301, 310, 500]
        moderate_rains = [302, 311, 501, 520]
        heavy_rains = [312, 313, 314, 321, 502, 503, 504, 520, 521, 522, 531]
        if weather_id >= 200 and weather_id <=232 :
            img = ImageTk.PhotoImage(Image.open('thunderstorm.png'))
            panel = Label(root, image=img)
            panel.image = img
            panel.place(x=350, y=200)
        elif weather_id==511 or (weather_id>=600 and weather_id<=622) :
            img = ImageTk.PhotoImage(Image.open('snow.png'))
            panel = Label(root, image=img)
            panel.image = img
            panel.place(x=350, y=200)
        elif weather_id in light_rains:
            img = ImageTk.PhotoImage(Image.open('light rain.png'))
            panel = Label(root, image=img)
            panel.image = img
            panel.place(x=350, y=200)
        elif weather_id in moderate_rains:
            img = ImageTk.PhotoImage(Image.open('moderate rain.png'))
            panel = Label(root, image=img)
            panel.image = img
            panel.place(x=350, y=200)
        elif weather_id in heavy_rains:
            img = ImageTk.PhotoImage(Image.open('heavy rain.png'))
            panel = Label(root, image=img)
            panel.image = img
            panel.place(x=350, y=200)
        elif wind_speed!='':
            if float(wind_speed)>8.88:
                img = ImageTk.PhotoImage(Image.open('windy.png'))
                panel = Label(root, image=img)
                panel.image = img
                panel.place(x=350, y=200)
        elif weather_id==800:
            img = ImageTk.PhotoImage(Image.open('clear sky.png'))
            panel = Label(root, image=img)
            panel.image = img
            panel.place(x=350, y=200)
        elif weather_id==801:
            img = ImageTk.PhotoImage(Image.open('partly cloudy.png'))
            panel = Label(root, image=img)
            panel.image = img
            panel.place(x=350, y=200)
        elif weather_id==802:
            img = ImageTk.PhotoImage(Image.open('cloudy.png'))
            panel = Label(root, image=img)
            panel.image = img
            panel.place(x=350, y=200)
        elif weather_id==803 or weather_id==804:
            img = ImageTk.PhotoImage(Image.open('overcast.png'))
            panel = Label(root, image=img)
            panel.image = img
            panel.place(x=350, y=200)
        else:
            img = ImageTk.PhotoImage(Image.open('foggy.png'))
            panel = Label(root, image=img)
            panel.image = img
            panel.place(x=350, y=200)
    except KeyError:
        lable_citi.configure(text='Error - Invalid Input', fg='#f00')
        lable_country.configure(text='')
        lable_temp.configure(text='')
        lable_precip.configure(text='')
        lable_descr.configure(text='')
        lable_humidity.configure(text='')
        max_temp.configure(text='')
        min_temp.configure(text='')
        lable_pressure.configure(text='')
        lable_wind.configure(text='')
        lable_wind_dir.configure(text='')
        lable_sunrise.configure(text='')
        lable_sunset.configure(text='')
        humi.configure(text='')
        maxi.configure(text='')
        mini.configure(text='')
        pressure.configure(text='')
        wind.configure(text='')
        wind_dir.configure(text='')
        sunrise_time.configure(text='')
        sunset_time.configure(text='')        
    

# Search / shortcut buttons
######  Change sizes
city_nameButton = Button(root, text="Search", command= lambda: city_name(False,False))
city_nameButton.place(x=300, y=100)

home_Button = Button(root, text='Home', command= lambda: city_name(True,False))
home_Button.place(x=450, y=100)

uni_Button = Button(root, text='Uni', command= lambda: city_name(False,True))
uni_Button.place(x=500, y=100)


var = IntVar()

adv_inf_Button = Checkbutton(root, text='Advanced Information', variable=var,
                             onvalue=1, offvalue=0, command=is_on)
adv_inf_Button.place(x=25, y=450)

# Country/Place Names
###### Update positions / Only show once search occurs
lable_citi = Label(root, text="...", width=0, 
                   bg='white', font=("Times New Roman", 15))
lable_citi.place(x=25, y=150)
 
lable_country = Label(root, text="...", width=0, 
                      bg='white', font=("Times New Roman", 15)) ## Places objects
lable_country.place(x=200, y=150)
 

# Current Temperature
 
lable_temp = Label(root, text="...", width=0, bg='white',
                   font=("Times New Roman", 30), fg='black')
lable_temp.place(x=25, y=220)

lable_precip = Label(root, text='...', width=0, bg='white',
                   font=("Times New Roman", 30), fg='black')
lable_precip.place(x=25, y=280)

lable_descr = Label(root, text='...', width=0, bg='white',
                   font=("Times New Roman", 30), fg='black')
lable_descr.place(x=25, y=340)
 
# Other temperature details
humi = Label(root, text="", width=0, 
                        bg='white', font=("Times New Roman", 15))
humi.place(x=25, y=495)
                     
lable_humidity = Label(root, text="", width=0,
                        bg='white', font=("Times New Roman", 15))
lable_humidity.place(x=150, y=495)
                     

maxi = Label(root, text="", width=0, 
                        bg='white', font=("Times New Roman", 15))
maxi.place(x=25, y=545)
                     
max_temp = Label(root, text="", width=0, 
                        bg='white', font=("Times New Roman", 15))
max_temp.place(x=150, y=545)
                     
                     
mini = Label(root, text="", width=0, 
                        bg='white', font=("Times New Roman", 15))
mini.place(x=25, y=595)
                     
min_temp = Label(root, text="", width=0, 
                        bg='white', font=("Times New Roman", 15))
min_temp.place(x=150, y=595)

pressure = Label(root, text='', width=0, bg='white', font=('Times New Roman',15))
pressure.place(x=25, y= 645)

lable_pressure = Label(root, text='', width=0, bg='white', font=('Times New Roman',15))
lable_pressure.place(x=150, y=645)

wind = Label(root, text='', width=0, bg='white', font=('Times New Roman',15))
wind.place(x=325, y=495)

lable_wind = Label(root, text='', width=0, bg='white', font=('Times New Roman',15))
lable_wind.place(x=475, y=495)

wind_dir = Label(root, text='', width=0, bg='white', font=('Times New Roman',15))
wind_dir.place(x=325, y=545)

lable_wind_dir = Label(root, text='', width=0, bg='white', font=('Times New Roman',15))
lable_wind_dir.place(x=475, y=545)

sunrise_time = Label(root, text='', width=0, bg='white', font=('Times New Roman',15))
sunrise_time.place(x=325, y= 595)

lable_sunrise = Label(root, text='', width=0, bg='white', font=('Times New Roman',15))
lable_sunrise.place(x=475, y= 595)

sunset_time = Label(root, text='', width=0, bg='white', font=('Times New Roman',15))
sunset_time.place(x=325, y= 645)

lable_sunset = Label(root, text='', width=0, bg='white', font=('Times New Roman',15))
lable_sunset.place(x=475, y= 645)


root.mainloop()
