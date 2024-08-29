# python3 -- Weather Application using API
 
# importing the libraries
from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image


root = Tk()
root.title("Weather App") ## Create the main box pop up with specified dims.
root.geometry("600x800")
root['background'] = "White"

dt = datetime.datetime.now() ## Get date info
day = Label(root, text=dt.strftime('%A'), bg='white', font=("Times New Roman", 20))
day.place(x=25, y=25) ## %A gets the day, others are explanatory
date = Label(root, text=dt.strftime('%d/%m/%Y'), bg='white', font=("Times New Roman", 20))
date.place(x=200, y=25) 

hour = Label(root, text=dt.strftime('%I : %M %p'),
             bg='white', font=("Times New Roman", 20))
hour.place(x=400, y=25)

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

        location = api_forecast['city']
        city = location['name']
        country = location['country']

        lable_country.configure(text=country)
        lable_city.configure(text=city, fg='#000')

        lable_titles.configure(text='%-10s%12s%19s%20s'%('  Times', 'Temp. (°C)',
                                                         'Descr.', 'Rain (mm)'))
                                                         
        
        list_of_data = api_forecast['list']
        date_list = []
        temp_list = []
        desc_list = []
        rain_list = []
        id_list = []
        for i in range(len(list_of_data)):
            data = list_of_data[i]
            date_list += [data['dt_txt']]
            temp_list += [data['main']['temp']]
            desc_list += [data['weather'][0]['description']]
            id_list += [data['weather'][0]['id']]
            try:
                rain = data['rain']['3h']
                rain_list += [rain]
            except KeyError:
                rain_list += [0]
                
        day_list = []
        for i in date_list:
            day = i.split(' ')[0]
            if day not in day_list:
                day_list += [day]
                
        menubutton = Menubutton(root, text='  Forecast  ')
        menubutton.place(x=25,y=140)

        menu = Menu(menubutton)

        menu.add_command(label=day_list[0], command=lambda: handle_click(date_list,day_list[0],temp_list,desc_list,rain_list,id_list))
        menu.add_command(label=day_list[1], command=lambda: handle_click(date_list,day_list[1],temp_list,desc_list,rain_list,id_list))
        menu.add_command(label=day_list[2], command=lambda: handle_click(date_list,day_list[2],temp_list,desc_list,rain_list,id_list))
        menu.add_command(label=day_list[3], command=lambda: handle_click(date_list,day_list[3],temp_list,desc_list,rain_list,id_list))
        menu.add_command(label=day_list[4], command=lambda: handle_click(date_list,day_list[4],temp_list,desc_list,rain_list,id_list))
        menu.add_command(label=day_list[5], command=lambda: handle_click(date_list,day_list[5],temp_list,desc_list,rain_list,id_list))

        menubutton.config(menu=menu)
    except KeyError:
        
        lable_city.configure(text='Error - Invalid Input',fg='#f00')
        lable_country.configure(text='')
        
        img = ImageTk.PhotoImage(Image.open('blank.png'))
        panel1 = Label(root, image=img)
        panel1.img = img
        panel1.place(x=500, y=200)
        label1.configure(text='')
        panel2 = Label(root, image=img)
        panel2.img = img
        panel2.place(x=500, y=275)
        label2.configure(text='')
        panel3 = Label(root, image=img)
        panel3.img = img
        panel3.place(x=500, y=350)
        label3.configure(text='')
        panel4 = Label(root, image=img)
        panel4.img = img
        panel4.place(x=500, y=425)
        label4.configure(text='')
        panel5 = Label(root, image=img)
        panel5.img = img
        panel5.place(x=500, y=500)
        label5.configure(text='')
        panel6 = Label(root, image=img)
        panel6.img = img
        panel6.place(x=500, y=575)
        label6.configure(text='')
        panel7 = Label(root, image=img)
        panel7.img = img
        panel7.place(x=500, y=650)
        label7.configure(text='')
        panel8 = Label(root, image=img)
        panel8.img = img
        panel8.place(x=500, y=725)
        label8.configure(text='')

        

def icon(weather_id):
    light_rains = [300, 301, 310, 500]
    moderate_rains = [302, 311, 501, 520]
    heavy_rains = [312, 313, 314, 321, 502, 503, 504, 520, 521, 522, 531]
    if weather_id >= 200 and weather_id <=232 :
        img = 'thunderstorm 2.png'
    elif weather_id==511 or (weather_id>=600 and weather_id<=622) :
        img = 'snow 2.png'
    elif weather_id in light_rains:
        img = 'light rain 2.png'
    elif weather_id in moderate_rains:
        img = 'moderate rain 2.png'
    elif weather_id in heavy_rains:
        img = 'heavy rain 2.png'
    elif weather_id==800:
        img = 'clear sky 2.png'
    elif weather_id==801:
        img = 'partly cloudy 2.png'
    elif weather_id==802:
        img = 'cloudy 2.png'
    elif weather_id==803 or weather_id==804:
        img = 'overcast 2.png'
    else:
        img = 'foggy 2.png'

    return img
    

def handle_click(dates, day, temps, descs, rains, ids):

    day_list = []
    index1 = 0
    index_list = []
    for i in range(len(dates)):
        date = dates[i].split(' ')[0]
        if date not in day_list:
            day_list += [date]
        if date == day:
            index = i
            if index not in index_list:
                index_list += [index]
        
    for i in index_list:
        
        text1 = ""
        text2 = ""
        text3 = ""
        text4 = ""
        text5 = ""
        text6 = ""
        text7 = ""
        text8 = ""
        
        img1 = ImageTk.PhotoImage(Image.open('blank.png'))
        img2 = ImageTk.PhotoImage(Image.open('blank.png'))
        img3 = ImageTk.PhotoImage(Image.open('blank.png'))
        img4 = ImageTk.PhotoImage(Image.open('blank.png'))
        img5 = ImageTk.PhotoImage(Image.open('blank.png'))
        img6 = ImageTk.PhotoImage(Image.open('blank.png'))
        img7 = ImageTk.PhotoImage(Image.open('blank.png'))
        img8 = ImageTk.PhotoImage(Image.open('blank.png'))

        if len(index_list)>=1:
            text1 = '%-10s%9.2f%25s%15s'%(dates[index_list[0]].split(' ')[1], temps[index_list[0]], descs[index_list[0]].title(),"{:.2f}".format(rains[index_list[0]]))
            img1 = ImageTk.PhotoImage(Image.open(icon(ids[index_list[0]])))
        if len(index_list)>=2:
            text2 = '%-10s%9.2f%25s%15s'%(dates[index_list[1]].split(' ')[1], temps[index_list[1]], descs[index_list[1]].title(),"{:.2f}".format(rains[index_list[1]]))
            img2 = ImageTk.PhotoImage(Image.open(icon(ids[index_list[1]])))
        if len(index_list)>=3:
            text3 = '%-10s%9.2f%25s%15s'%(dates[index_list[2]].split(' ')[1], temps[index_list[2]], descs[index_list[2]].title(),"{:.2f}".format(rains[index_list[2]]))
            img3 = ImageTk.PhotoImage(Image.open(icon(ids[index_list[2]])))
        if len(index_list)>=4:
            text4 = '%-10s%9.2f%25s%15s'%(dates[index_list[3]].split(' ')[1], temps[index_list[3]], descs[index_list[3]].title(),"{:.2f}".format(rains[index_list[3]]))
            img4 = ImageTk.PhotoImage(Image.open(icon(ids[index_list[3]])))
        if len(index_list)>=5:
            text5 = '%-10s%9.2f%25s%15s'%(dates[index_list[4]].split(' ')[1], temps[index_list[4]], descs[index_list[4]].title(),"{:.2f}".format(rains[index_list[4]]))
            img5 = ImageTk.PhotoImage(Image.open(icon(ids[index_list[4]])))
        if len(index_list)>=6:
            text6 = '%-10s%9.2f%25s%15s'%(dates[index_list[5]].split(' ')[1], temps[index_list[5]], descs[index_list[5]].title(),"{:.2f}".format(rains[index_list[5]]))
            img6 = ImageTk.PhotoImage(Image.open(icon(ids[index_list[5]])))
        if len(index_list)>=7:
            text7 = '%-10s%9.2f%25s%15s'%(dates[index_list[6]].split(' ')[1], temps[index_list[6]], descs[index_list[6]].title(),"{:.2f}".format(rains[index_list[6]]))
            img7 = ImageTk.PhotoImage(Image.open(icon(ids[index_list[6]])))
        if len(index_list)>=8:
            text8 = '%-10s%9.2f%25s%15s'%(dates[index_list[7]].split(' ')[1], temps[index_list[7]], descs[index_list[7]].title(),"{:.2f}".format(rains[index_list[7]]))
            img8 = ImageTk.PhotoImage(Image.open(icon(ids[index_list[7]])))

        panel1 = Label(root, image=img1)
        panel1.img = img1
        panel1.place(x=500, y=200)
        
        panel2 = Label(root, image=img2)
        panel2.img = img2
        panel2.place(x=500, y=275)
        
        panel3 = Label(root, image=img3)
        panel3.img = img3
        panel3.place(x=500, y=350)
        
        panel4 = Label(root, image=img4)
        panel4.img = img4
        panel4.place(x=500, y=425)
        
        panel5 = Label(root, image=img5)
        panel5.img = img5
        panel5.place(x=500, y=500)
        
        panel6 = Label(root, image=img6)
        panel6.img = img6
        panel6.place(x=500, y=575)
        
        panel7 = Label(root, image=img7)
        panel7.img = img7
        panel7.place(x=500, y=650)
        
        panel8 = Label(root, image=img8)
        panel8.img = img8
        panel8.place(x=500, y=725)
        
        label1.configure(text=text1)
        label2.configure(text=text2)
        label3.configure(text=text3)
        label4.configure(text=text4)
        label5.configure(text=text5)
        label6.configure(text=text6)
        label7.configure(text=text7)
        label8.configure(text=text8)
        
    menubutton = Menubutton(root, text=day)
    menubutton.place(x=25,y=140)
    menu = Menu(menubutton)
    
    menu.add_command(label=day_list[0], command=lambda: handle_click(dates,day_list[0],temps,descs,rains,ids))
    menu.add_command(label=day_list[1], command=lambda: handle_click(dates,day_list[1],temps,descs,rains,ids))
    menu.add_command(label=day_list[2], command=lambda: handle_click(dates,day_list[2],temps,descs,rains,ids))
    menu.add_command(label=day_list[3], command=lambda: handle_click(dates,day_list[3],temps,descs,rains,ids))
    menu.add_command(label=day_list[4], command=lambda: handle_click(dates,day_list[4],temps,descs,rains,ids))
    menu.add_command(label=day_list[5], command=lambda: handle_click(dates,day_list[5],temps,descs,rains,ids))

    menubutton.config(menu=menu)
    times = []
    for i in dates:
        if day in i:
            times += [i.split(' ')[1]]


city_nameButton = Button(root, text="Search", command= lambda: city_name(False,False))
city_nameButton.place(x=300, y=100)

home_Button = Button(root, text='Home', command= lambda: city_name(True,False))
home_Button.place(x=450, y=100)

uni_Button = Button(root, text='Uni', command= lambda: city_name(False,True))
uni_Button.place(x=500, y=100)

lable_titles = Label(root, text="", width=0, 
                   bg='white', font=("Times New Roman", 15, 'underline'))
lable_titles.place(x=25, y=175)

lable_city = Label(root, text="", width=0, 
                   bg='white', font=("Times New Roman", 15))
lable_city.place(x=150, y=140)
 
lable_country = Label(root, text="", width=0, 
                      bg='white', font=("Times New Roman", 15)) ## Places objects
lable_country.place(x=325, y=140)

label1 = Label(root, text="", width=0, 
                        bg='white', font=("Times New Roman", 15))
label1.place(x=25, y=220)

label2 = Label(root, text="", width=0, 
                        bg='white', font=("Times New Roman", 15))
label2.place(x=25, y=295)

label3 = Label(root, text="", width=0, 
                        bg='white', font=("Times New Roman", 15))
label3.place(x=25, y=370)

label4 = Label(root, text="", width=0, 
                        bg='white', font=("Times New Roman", 15))
label4.place(x=25, y=445)

label5 = Label(root, text="", width=0, 
                        bg='white', font=("Times New Roman", 15))
label5.place(x=25, y=520)

label6 = Label(root, text="", width=0, 
                        bg='white', font=("Times New Roman", 15))
label6.place(x=25, y=595)

label7 = Label(root, text="", width=0, 
                        bg='white', font=("Times New Roman", 15))
label7.place(x=25, y=670)

label8 = Label(root, text="", width=0, 
                        bg='white', font=("Times New Roman", 15))
label8.place(x=25, y=745)
    
root.mainloop()
    
