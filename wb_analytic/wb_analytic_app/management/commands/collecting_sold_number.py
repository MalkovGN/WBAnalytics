import random
import time
import requests

from django.core.management.base import BaseCommand

from wb_analytic_app.management.commands.collect_prod_nums import proxies, times_sleeps
from wb_analytic_app.models import ProductInfo, AmountProductsNotSaved


def collecting_sold_numbers():
    """
    Collecting amount of sold
    products
    """
    time_start = time.time()
    products = ProductInfo.objects.all()

    for product in products:
        vendor_code = product.product_id
        proxy = random.choice(proxies)
        time.sleep(random.choice(times_sleeps))
        url = f'https://product-order-qnt.wildberries.ru/by-nm/?nm={vendor_code}'
        print(url)

        try:
            response = requests.get(url=url, proxies=proxy)
            qnt = response.json()[0]['qnt']
            # product_id = product.pk
            ProductInfo.objects.filter(product_id=product.pk).update(
                sold_number=qnt,
            )
            # product_amount = ProductInfo.objects.filter(p
            #     sold_number=qnt,
            # )
            # # product_amount.save()
        except Exception:
            product_amount_not_saved = AmountProductsNotSaved(
                product_id=product.product_id,
                name=product.name,
                category_id=product.category_id,
            )
            product_amount_not_saved.save()
            print(f'Product {product.name} didnt save!!!')
    print(f'The program was executed {time.time() - time_start} s.')


class Command(BaseCommand):
    def handle(self, *args, **options):
        collecting_sold_numbers()
