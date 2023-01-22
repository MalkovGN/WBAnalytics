import random
import time
import requests

from django.core.management.base import BaseCommand

from wb_analytic_app.models import CategoriesNotSaved, ProductInfo, CategoryPageInfo
from wb_analytic_app.management.commands.collect_prod_nums import proxies, times_sleeps


def collect_product_info():
    time_start = time.time()
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

            print(f'Category {category.name} saved successfully!')
        except Exception:
            not_saved_category = CategoriesNotSaved(
                name=category.name,
                wb_url=category.wb_url,
                first_page_products_url=category.first_page_products_url,
            )
            not_saved_category.save()
            print(f'Category {category.name} didnt save!!!')
    print(f'The program was executed {time.time() - time_start} s.')


class Command(BaseCommand):
    def handle(self, *args, **options):
        collect_product_info()
