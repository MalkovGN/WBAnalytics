import json
import os
import requests
import random
import time

from wb_analytic_app.models import CategoryPageInfo, CategoriesNotSaved, ProductInfo, AmountProductsNotSaved
from wb_analytic_app.file import proxies, times_sleeps


class JsonParser:
    """
    Subcategories json parser class
    Getting unique subcategory_info
    """
    def __init__(self, data):
        self.data = data
        self.subcategory_info = []

    def start(self):
        if 'childs' in self.data.keys():
            self.unpack(self.data['childs'])
        else:
            if self.data['url'].startswith('/'):
                try:
                    self.subcategory_info.append(
                        {
                            'name': self.data['name'],
                            'url': 'https://www.wildberries.ru' + self.data['url'],
                            'shard': self.data['shard'],
                            'query': self.data['query'],
                        }
                    )
                except KeyError:
                    self.subcategory_info.append(
                        {
                            'name': self.data['name'],
                            'url': 'https://www.wildberries.ru' + self.data['url'],
                        }
                    )
            else:
                self.subcategory_info.append(
                    {
                        'name': self.data['name'],
                        'url':  self.data['url'],
                    }
                )

    def unpack(self, sub_category):
        for element in sub_category:
            if 'childs' in element.keys():
                element = element['childs']
                self.unpack(element)
            else:
                if element['url'].startswith('/'):
                    try:
                        self.subcategory_info.append(
                            {
                                'name': element['name'],
                                'url': 'https://www.wildberries.ru' + element['url'],
                                'shard': element['shard'],
                                'query': element['query'],
                            }
                        )
                    except KeyError:
                        self.subcategory_info.append(
                            {
                                'name': element['name'],
                                'url': 'https://www.wildberries.ru' + element['url'],
                            }
                        )
                else:
                    self.subcategory_info.append(
                        {
                            'name': element['name'],
                            'url': element['url'],
                        }
                    )


def collect_all_urls():
    """
    Parse a json file with categories
    :return: A list of unique subcategories subcategory_info
    """
    with open(f'{os.getcwd()}/wb_analytic_app/static/wb_analytic_app/categories_info.json', 'r', encoding='utf-8') as file:
        data_json = json.load(file)

    all_urls = []

    for elem in data_json:
        test_json = JsonParser(elem)
        test_json.start()
        all_urls += test_json.subcategory_info

    # print(all_urls)
    # print(len(all_urls))
    return all_urls


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
            subject_query = query
        else:
            continue

        url = f'https://catalog.wb.ru/catalog/{shard}/v4/filters?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&{kind_query}&lang=ru&locale=ru&pricemarginCoeff=1.0&reg=0&regions=80,64,83,4,38,33,70,68,69,86,75,30,40,48,1,66,31,22,71&spp=0&{subject_query}'
        subcategory_name = subcategory['name']
        urls_list.append({subcategory_name: url})

    # print(urls_list)
    # print(len(urls_list))
    return urls_list


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


def collect_page_info():
    """
    Saving to database
    1) Category name
    2) wb_url
    3) url to first page products info
    """
    subcategories_info = collect_all_urls()
    s1 = get_full_info_categories(subcategories_info)

    for elem in s1:
        name = elem['name']
        wb_url = elem['url']
        shard = elem['shard']
        query = elem['query']
        split_query = query.split('&')
        page_number = 1  # When I will know how many pages
        # I need to get -- CHANGE IT
        if split_query[0][:4] == 'kind':
            kind_query = split_query[0]
            subject_query = split_query[1]
        elif split_query[0][:4] == 'subj':
            kind_query = ''
            subject_query = query
        else:
            continue
        first_page_products_url = f'https://catalog.wb.ru/catalog/{shard}/catalog?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&{kind_query}&lang=ru&locale=ru&page={page_number}&pricemarginCoeff=1.0&reg=0&regions=80,64,83,4,38,33,70,68,69,86,75,30,40,48,1,66,31,22,71&spp=0&{subject_query}'

        page_info = CategoryPageInfo(
            name=name,
            wb_url=wb_url,
            first_page_products_url=first_page_products_url,
        )
        page_info.save()


def collect_product_info():
    categories = CategoryPageInfo.objects.all()

    for category in categories:
        url = category.first_page_products_url
        # print(url)
        proxy = random.choice(proxies)
        # print(proxy)
        time.sleep(random.choice(times_sleeps))

        try:
            response = requests.get(url=url, proxies=proxy)
            time.sleep(random.choice(times_sleeps))
            products = response.json()['data']['products']
            for product in products:
                # print(product['id'], product['name'], product['feedbacks'], product['priceU'], product['salePriceU'], '\n')
                product_info = ProductInfo(
                    product_id=product['id'],
                    name=product['name'],
                    feedbacks=product['feedbacks'],
                    sale_price=product['salePriceU'],
                    price=product['priceU'],
                    category_id=category.pk,
                )
                product_info.save()

        except Exception:
            not_saved_category = CategoriesNotSaved(
                name=category.name,
                wb_url=category.wb_url,
                first_page_products_url=category.first_page_products_url,
            )
            not_saved_category.save()


def retry_saving_sold_numbers():
    """
    Sending requests again
    in products, which weren't saved
    """
    products_not_saved = AmountProductsNotSaved.objects.all()

    for product in products_not_saved:
        vendor_code = product.product_id
        url = f'https://product-order-qnt.wildberries.ru/by-nm/?nm={vendor_code}'
        proxy = random.choice(proxies)
        time.sleep(random.choice(times_sleeps))

        try:
            response = requests.get(url=url, proxies=proxy)
            qnt = response.json()[0]['qnt']
            ProductInfo.objects.filter(pk=product.pk).update(
                sold_number=qnt,
            )
            AmountProductsNotSaved.objects.filter(pk=product.pk).delete()
            print(f'Product {product.name} saved!')
        except Exception:
            print(f'Product {product.name} with vendor code {product.product_id} didnt save')