#! /usr/bin/env python
# -*- coding: utf-8 -*-


import database
import requests
from bs4 import BeautifulSoup
import time
import pprint

links = database.get_sheet('godness', 'links')
actors_info = database.get_sheet('godness', 'actors_info')


def get_item_info(url):
    web_data = ''
    while web_data == '':
        try:
            web_data = requests.get(url)
        except:
            print('web_site is tired, let us sleep for 5 second')
            print('zzZZ')
            time.sleep(5)
            continue
    soup = BeautifulSoup(web_data.content, 'lxml')
    name = soup.find('h1').text if soup.find('h1') else None
    print(name+':'+url)
    numbers = soup.select('b') if soup.select('b') else None
    dates = soup.select('span > date:nth-of-type(2)') if soup.select('span > date:nth-of-type(2)') else None
    titles = soup.select('div > div > span > p') if soup.select('div > div > span > p') else None
    for number, date, title in zip(numbers, dates, titles):
        data = {
            'name': name,
            'number': number.text,
            'date': date.text,
            'title': title.text
        }
        actors_info.insert_one(data)


def get_all_info():
    while links.count() > 0:
        time.sleep(1)
        url = links.find_one()['url']
        get_item_info(url)
        links.delete_one({})

get_all_info()





