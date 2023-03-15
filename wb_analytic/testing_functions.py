import os
import random
import time
import datetime
import requests
import json
# from json_parser import JsonParser
from services.json_parser import JsonParser
from check_proxy import LOGIN, PASSWORD

# from wb_analytic_app.models import ProductsNumberUrlsModel

proxies = {
    'https': f'http://{LOGIN}:{PASSWORD}@195.216.132.9:8000'
}


def collect_main_page_data(url):
    """
    To make a proxy info more safety !!!
    :param url: to categories json file
    :return: creating/updating json file
    """

    proxies = {
        'https': f'http://{LOGIN}:{PASSWORD}@195.216.132.9:8000'
    }
    response = requests.get(url=url, proxies=proxies)
    with open(f'{os.getcwd()}/wb_analytic_app/static/wb_analytic_app/categories_info.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def collect_all_urls():
    """
    Parse a json file with categories
    :return: A list of unique subcategories subcategory_info
    """
    with open('categories_info.json', 'r', encoding='utf-8') as file:
        data_json = json.load(file)

    all_urls = []

    for elem in data_json:
        test_json = JsonParser(elem)
        test_json.start()
        all_urls += test_json.subcategory_info

    # print(all_urls)
    # print(len(all_urls))
    return all_urls


def get_categories_without_shard(subcategories_info):
    """
    :param subcategories_info: JSON with all subcategories
    :return: The list with subcategories which has not
    shard and query params
    """
    categories_without_shard = []

    for subcategory in subcategories_info:
        if 'shard' not in subcategory.keys():
            categories_without_shard.append(subcategory)

    # print(categories_without_shard)
    # print(len(categories_without_shard))
    return categories_without_shard


def get_full_info_categories(subcategories_info):
    """
    :param subcategories_info: JSON with all subcategories
    :return: The list only with shard and query params
    """
    full_info_subcategories = []

    for subcategory in subcategories_info:
        if 'shard' not in subcategory.keys():
            continue
        else:
            full_info_subcategories.append(subcategory)
    print(full_info_subcategories)
    print(len(full_info_subcategories))
    return full_info_subcategories


def number_of_products_links(subcategories_info):
    """
    Creating list of urls to check
    number of products in subcategory
    :param subcategories_info: JSON with
     subcategories params
    :return: The list of urls
    """
    urls_list = []
    for subcategory in subcategories_info:
        shard = subcategory['shard']
        query = subcategory['query']
        split_query = query.split('&')
        if split_query[0][:4] == 'kind':
            kind_query = split_query[0]
            subject_query = split_query[1]
        elif split_query[0][:4] == 'subj':
            kind_query = ''
            subject_query = query
        else:
            continue

        url = f'https://catalog.wb.ru/catalog/{shard}/v4/filters?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&{kind_query}&lang=ru&locale=ru&pricemarginCoeff=1.0&reg=0&regions=80,64,83,4,38,33,70,68,69,86,75,30,40,48,1,66,31,22,71&spp=0&{subject_query}'
        subcategory_name = subcategory['name']
        # if shard == 'babies':
        urls_list.append({subcategory_name: url})
        # else:
        #     continue


    # print(urls_list)
    # print(len(urls_list))
    return urls_list


def collect_url_items():
    """
    Collecting from url the values
    of shard and query
    """
    s = 'https://catalog.wb.ru/catalog/outwear1/v4/filters?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&kind=2&lang=ru&locale=ru&pricemarginCoeff=1.0&reg=0&regions=80,64,83,4,38,33,70,68,69,86,75,30,40,48,1,66,31,22,71&spp=0&subject=168;170;171;172;173;174;193;289;322;1591;1629;1630;1631;1633;1635;1641;1791;2110;4315;4377;8098;8239'
    s1 = 'https://catalog.wb.ru/catalog/shealth3/v4/filters?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&&lang=ru&locale=ru&pricemarginCoeff=1.0&reg=0&regions=80,64,83,4,38,33,70,68,69,86,75,30,40,48,1,66,31,22,71&spp=0&subject=369;835;837;1329;1330;1331;1332;1333;1334;1335;1336;1341;2377;3078;3720;3739;4370;4371;4372;4373;5099;5550;5934'
    s2 = 'https://catalog.wb.ru/catalog/women_shoes2/v4/filters?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&kind=2&lang=ru&locale=ru&pricemarginCoeff=1.0&reg=0&regions=80,64,83,4,38,33,70,68,69,86,75,30,40,48,1,66,31,22,71&spp=0&subject=104;105;128;130;232;396;1382'
    s3 = 'https://catalog.wb.ru/catalog/sport14/v4/filters?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&&lang=ru&locale=ru&pricemarginCoeff=1.0&reg=0&regions=80,64,83,4,38,33,70,68,69,86,75,30,40,48,1,66,31,22,71&spp=0&subject=1303;1315;1390;1406;3589;5696'
    first_split = s.split('?')
    print(first_split)
    second_split = first_split[1].split('&')
    print(second_split)
    query = ''
    for elem in second_split:
        if 'kind' in elem.split('='):
            query += elem + '&'
        if 'subject' in elem.split('='):
            idx = second_split.index(elem)
            for i in range(idx, len(second_split)):
                query += second_split[i] + '&'

    print(query[:-1])
    counter = 0
    shard = ''
    for elem in first_split[0]:
        # print(elem)
        if elem == '/':
            counter += 1
        if counter == 4:
            shard += elem
    print(shard[1:])


def get_num_products(url):
    response = requests.get(url, proxies=proxies)
    print(response.json()['data']['total'])


def parse_category_json():
    url = 'https://catalog.wb.ru/catalog/bl_shirts/catalog?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&kind=2&lang=ru&locale=ru&page=1&pricemarginCoeff=1.0&reg=0&regions=80,64,83,4,38,33,70,68,69,86,75,30,40,48,1,66,31,22,71&spp=0&subject=41;184;1429'
    response = requests.get(url=url, proxies=proxies)
    print(response.json())
    return response.json()


# if __name__ == '__main__':
    # url = 'https://product-order-qnt.wildberries.ru/by-nm/?nm=13988939'
    # response = requests.get(url=url, proxies=proxies)
    # print(response.json())
    # pass
    # print(datetime.date.today())
    # print(collect_all_urls())
# class Bank:
#     def __init__(self, name, date):
#         self.name = name
#         self.date = date
#     def __str__(self):
#         return self.name + self.date
#
# sber = Bank("Sberbank", "1841")
# x =str(sber)
# print(x)

# def foo(y, x) -> bool:
#     y.append(str(x))
#     return x % 2
# y = ["sber", "bank"]
# print([x for x in range(len(y)) if foo(y, x)])

# x = 1,2,3
# x == 4,5,6
# print(x)

# print(0 or 'sber', end='')
# print(1841 or 'sber')

# x = {1: "sber", 2: "bank", 3: None}
# y = x.keys()
# print(y)

# def sber(s=[]) -> []:
#     s.append("sber")
#     return s
# sber()
# sber(["bank"])
# result = sber() + sber(["bank"])
# print(result)

# def append(my_list):
#     my_list = [0, 0]
#     my_list[0] = 1
#     return 2
# my_list = (0, 1)
# my_list[0] = append(my_list)
# print(my_list)

x = 0
try:
    print(x/0)
except ZeroDivisionError:
    print(x+1, sep='')
except ZeroDivisionError:
    print(x+2, sep='')
except ZeroDivisionError:
    print(x+3, sep='')