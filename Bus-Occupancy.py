from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date
import calendar
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

WEEKENDER = 2620

url = "https://routes.uga.edu/Route/" + str(WEEKENDER) + "/Vehicles"

r = requests.get(url)
data = r.json()
print(data)
list_data = list(data)

bus1 = list_data[1]

bus1_list = list(bus1)
print(bus1_list[2])



