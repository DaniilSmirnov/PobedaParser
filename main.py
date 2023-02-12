import time
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from loguru import logger

origin = 'LED'

print('Destination IATA Code')
destination = input()

print('Wanted price')
wanted_price = int(input())

now_date = datetime.datetime.now() + datetime.timedelta(days=1)
search_date = now_date.date()


while str(search_date) != '2023-10-26':
    driver = webdriver.Chrome(executable_path='/Users/di.smirnov/PycharmProjects/pobedaParser/chromedriver')
    search_date = (search_date + datetime.timedelta(days=1))
    formated_date = str(search_date).split('-')
    formated_date = formated_date[2] + '.' + formated_date[1] + '.' + formated_date[0]
    url = "https://ticket.pobeda.aero/websky/?origin-city-code%5B0%5D=" + origin + "&destination-city-code%5B0%5D=" + destination + "&date%5B0%5D=" + formated_date + "&segmentsCount=1&adultsCount=1&youngAdultsCount=0&childrenCount=0&infantsWithSeatCount=0&infantsWithoutSeatCount=0&lang=ru#/search"

    driver.get(url)
    time.sleep(5)
    htmlSource = driver.page_source

    soup = BeautifulSoup(htmlSource)
    x = soup.find_all('span', attrs={'class': 'price-cell__text'})
    for item in x:
        price = item.text
        price = re.findall('\d', price)
        price = ''.join(price)
        price = int(price)
        if price < wanted_price:
            logger.info(str(price) + '   ' + url)
    driver.close()

    time.sleep(2)

