from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required ,logout_user, current_user
import urllib.request
import geocoder
import requests, json

views = Blueprint('views', __name__)

#define route - decorator @
@views.route('/')
def home():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print(external_ip)
    g = geocoder.ipinfo(external_ip)
    print(g.city)
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + g.city + "&appid=" + 'b23b2c4d66fefd13893e1d14f585a484'
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temp = round(main['temp'] - 273.15,2)
        humi = main['humidity']
        press = main['pressure']
        report = data['weather']
        print(temp)
        print(press)
        print(humi)
        print(report[0]['description'])
    else:
        print("didn't workout")

    return render_template("home.html", user=current_user)
