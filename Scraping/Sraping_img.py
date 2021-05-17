#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import os

os.makedirs('./img/', exist_ok=True)

URL = 'http://www.ngchina.com.cn/animals/'


html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('ul', {"class": "img_list"})



for ul in img_ul:
    imgs = ul.find_all("img")
    for img in imgs:
        url = img['src']
        if url == "":
            print(True)
        print(url)


for ul in img_ul:
    imgs = ul.find_all("img")
    for img in imgs:
        url = img['src']
        if url != "":
            r = requests.get(url, stream = True)
            image_name = url.split('/')[-1]
            with open('./img/%s' % image_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size = 128):
                    f.write(chunk)
            print('Saved %s' % image_name)

