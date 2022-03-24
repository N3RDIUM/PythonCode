from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(3)

def scrape():
    headers = ["vmag", "name", "bayer", "distance_ly", "spectral_class", "mass", "radius", "luminosity"]
    star_data = []

    soup = BeautifulSoup(browser.page_source, "html.parser")
    table = soup.find_all("table", attrs={"class", "wikitable sortable jquery-tablesorter"})[0]

    for row in table.find_all("tr"):
        cols = row.find_all("td")
        if len(cols) == 0:
            continue
        star_data.append([col.text.strip() for col in cols])

    with open("stars.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        # use for loop to write each row of data to csv
        for row in star_data:
            try:
                csvwriter.writerow(row)
            except:
                pass

scrape()
exit()