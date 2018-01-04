#! /usr/bin/env python
# -*- coding: utf-8 -*-


from get_all_normall_urls import normal_urls
import requests
from bs4 import BeautifulSoup
from database import get_sheet
import time


def get_all_links():
    sheet = get_sheet('godness', 'links')
    for url in normal_urls:
        sheet.insert_one({'url': url})
        print(url)
        time.sleep(0.5)
        for i in range(2, 50):
            index_url = url+'index_'+str(i)+'.html'
            web_data = requests.get(index_url)
            soup = BeautifulSoup(web_data.text, 'lxml')
            if soup.find('a'):
                print(index_url)
                sheet.insert_one({'url': index_url})
            else:
                break


