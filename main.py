import requests
import json
from json_parser import JsonParser
from check_proxy import LOGIN, PASSWORD


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
    with open('categories_info.json', 'w', encoding='utf-8') as file:
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
    # print(full_info_subcategories)
    # print(len(full_info_subcategories))
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
            subject_query = split_query[0]
        else:
            continue

        url = f'https://catalog.wb.ru/catalog/{shard}/v4/filters?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&{kind_query}&lang=ru&locale=ru&pricemarginCoeff=1.0&reg=0&regions=80,64,83,4,38,33,70,68,69,86,75,30,40,48,1,66,31,22,71&spp=0&{subject_query}'
        urls_list.append(url)

    # print(urls_list)
    # print(len(urls_list))
    return urls_list


if __name__ == '__main__':
    URL = 'https://static-basket-01.wb.ru/vol0/data/main-menu-ru-ru.json'
    # collect_main_page_data(URL)
    # collect_all_urls()
    subcategories_info = collect_all_urls()
    # get_categories_without_shard(subcategories_info)
    s1 = get_full_info_categories(subcategories_info)
    number_of_products_links(s1)
    # number_of_products_links()
