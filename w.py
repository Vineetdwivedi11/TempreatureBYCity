
import tkinter as tk
from urllib import response
from requests import request
from tkinter import font 
import requests


HEIGHT = 700
WIDTH = 600


def test_function(entry):
    print("This is entry:",entry)

def format_response(weather):
    print(weather)
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s  \nCondition: %s \nTemprature (C): %s' %(name, desc, temp)
    except:
        final_str = 'There was a Problem retreiving that information.'

    return final_str


def get_weather(city):
    weather_key = 'YOUR_API_KEY_HERE'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params= {'APPID': weather_key, 'q':city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])
    label['text']   = format_response(weather)


root   = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width= WIDTH)
canvas.pack()


#background_image = tk.PhotoImage(file="weather.jpg")
##background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame,text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg= '#80c1ff', bd =10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='white', font=40)
label.place(relwidth=1, relheight= 1)

root.mainloop()   
