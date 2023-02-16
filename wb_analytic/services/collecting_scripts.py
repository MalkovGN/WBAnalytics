import time

import requests
import json
import os
import random

from datetime import date

from services.proxies import proxies, times_sleeps
from services import secondary_scripts

from wb_analytic_app import models


def collect_main_page_data():
    """
    To make a proxy info more safety !!!
    url: to categories json file
    :return: creating/updating json file
    """
    secondary_scripts.clear_static_directory()
    url = 'https://static-basket-01.wb.ru/vol0/data/main-menu-ru-ru-v2.json'
    proxy = random.choice(proxies)
    response = requests.get(url=url, proxies=proxy)
    with open(f'{os.getcwd()}/services/static/services/categories_info_{date.today()}.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def collect_category_name_id():
    """
    Saving to db a name of
    category and unique id
    """
    subcategories_info = secondary_scripts.collect_main_info()
    s1 = secondary_scripts.get_full_info_categories(subcategories_info)

    for elem in s1:
        name = elem['name']
        category_id = elem['id']
        updated_values = {
            'shard': elem['shard'],
            'query': elem['query'],
            'wb_url': elem['url']
        }

        obj, created = models.CategoryNameModel.objects.update_or_create(
            name=name,
            category_id=category_id,
            defaults=updated_values,
        )


def collect_page_info():
    """
    Saving to database
    1) Category name
    2) wb_url
    3) url to first page products info
    4) Unique category id
    """
    categories = models.CategoryNameModel.objects.all()
    for category in categories:
        split_query = category.query.split('&')
        page_number = 1  # When I will know how many pages
        # I need to get -- CHANGE IT
        if split_query[0][:4] == 'kind':
            kind_query = split_query[0]
            subject_query = split_query[1]
        elif split_query[0][:4] == 'subj':
            kind_query = ''
            subject_query = category.query
        else:
            continue

        first_page_products_url = f'https://catalog.wb.ru/catalog/{category.shard}/catalog?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&{kind_query}&lang=ru&locale=ru&page={page_number}&pricemarginCoeff=1.0&reg=0&regions=80,64,83,4,38,33,70,68,69,86,75,30,40,48,1,66,31,22,71&spp=0&{subject_query}'
        updated_values = {'first_page_products_url': first_page_products_url}

        models.CategoryPageInfo.objects.update_or_create(
            name=category.name,
            category_id_id=category.pk,
            defaults=updated_values,
        )


def collect_product_info():
    categories = models.CategoryPageInfo.objects.all()

    for category in categories:
        request_url = category.first_page_products_url
        proxy = random.choice(proxies)
        time.sleep(random.choice(times_sleeps))

        try:
            response = requests.get(url=request_url, proxies=proxy)
            products = response.json()['data']['products']

            for product in products:
                update_values = {
                    'feedbacks': product['feedbacks'],
                    'sale_price': product['salePriceU'],
                    'price': product['priceU'],
                    'category_id_id': category.pk,
                }
                models.ProductInfo.objects.update_or_create(
                    product_id=product['id'],
                    name=product['name'],
                    defaults=update_values,

                )
            print(f'The category {category} saved successfully!')
        except Exception:
            not_saved_category = models.CategoriesNotSaved(
                name=category.name,
                first_page_products_url=category.first_page_products_url,
                category_id_id=category.pk,
            )
            not_saved_category.save()
            print(f'The category {category} didnt save!!!')
