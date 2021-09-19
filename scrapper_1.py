from bs4 import BeautifulSoup
import requests
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
time.sleep(10)
headers = ["Name", "Distance", "Mass", "Radius"]
star_data = []
new_star_data = []