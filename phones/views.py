from django.http import JsonResponse
from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


def getInfo(request):
    results=getData()
    return render(request,'phones/template.html',context={'results':results})

def getData():
    html = urlopen('https://www.digikala.com/search/category-mobile-phone/')
    soup = BeautifulSoup(html, 'html.parser')
    postings = soup.find_all("li", class_='c-listing__items js-plp-products-list')
    products=[]
    for item in postings:
        phoneName = item.find('li').find('div')['data-title-fa']
        phonePrice = item.find('li').find('div', class_='c-product-box')['data-price']
        phoneLink = item.find('li').find('div', class_='c-product-box').find('a')['href']
        phoneRowPrice = \
        item.find('li').find('div', class_='c-product-box').find('div', class_='c-product-box__content').find(
            'c-product-box__row').find('div').find('div')['del']
        productUrlimage = item.find('li').find('div').find('a')['href']
        products.append({'phoneName':phoneName,'phonePrice':phonePrice,'phoneLink':phoneLink,'phoneRowPrice':phoneRowPrice,
                     'procductURLImage':productUrlimage})
    return products
