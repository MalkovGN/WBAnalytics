import requests
import json
from bs4 import BeautifulSoup as Soup
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
    :return: A list of unique subcategories urls
    """
    with open('categories_info.json', 'r', encoding='utf-8') as file:
        data_json = json.load(file)

    all_urls = []

    for elem in data_json:
        test_json = JsonParser(elem)
        test_json.start()
        all_urls += test_json.urls

    print(all_urls)
    print(len(all_urls))
    return all_urls


if __name__ == '__main__':
    URL = 'https://static-basket-01.wb.ru/vol0/data/main-menu-ru-ru.json'
    collect_main_page_data(URL)
    collect_all_urls()
