import random
import requests
import time

from django.core.management.base import BaseCommand

from wb_analytic_app.services import collect_all_urls, get_full_info_categories, number_of_products_links, get_categories_without_shard
from wb_analytic_app.models import ProductsInCategory, ProductsNotSaved


LOGIN = '9cocbg'
PASSWORD = 'QJN879'

# LOGIN_CANADA = 'g9p4Qt'
# PASSWORD_CANADA = 'mDPk87'

LOGIN_USA = 'kVNGb0'
PASSWORD_USA = '1Xmss5'

LOGIN_RUSSIA_SHRD = 'nr2GNL'
PASSWORD_RUSSIA_SHRD = 'Y5qSRJ'

proxy_russia = {
    'https': f'http://{LOGIN}:{PASSWORD}@195.216.132.9:8000'
}

# proxy_canada = {
#     'https': f'http://{LOGIN_CANADA}:{PASSWORD_CANADA}@138.128.19.109:9999'
# }

proxy_usa = {
    'https': f'http://{LOGIN_USA}:{PASSWORD_USA}@181.177.103.207:9145'
}

proxy_russia_shared = {
    'https': f'http://{LOGIN_RUSSIA_SHRD}:{PASSWORD_RUSSIA_SHRD}@194.67.200.14:9741'
}


proxies = [proxy_usa, proxy_russia, proxy_russia_shared]
times_sleeps = [1.23, 2.03, 3.3, 4.21, 5.5]


def collect_number_of_products():
    """
    Saving to database name and
    number of products in category
    """
    subcategories_info = collect_all_urls()
    s1 = get_full_info_categories(subcategories_info)
    links = number_of_products_links(s1)

    for elem in links:
        url = list(elem.values())[0]
        prox = random.choice(proxies)

        try:
            response = requests.get(url, proxies=prox)
            time.sleep(random.choice(times_sleeps))
            products_in_category = ProductsInCategory(
                category=list(elem.keys())[0],
                counter=response.json()['data']['total'],
            )
            products_in_category.save()
            print(f'The product {list(elem.keys())[0]} saved successfully!')
        except Exception:
            not_saved_products = ProductsNotSaved(
                category=list(elem.keys())[0],
                url=url,
            )
            not_saved_products.save()
            print(f'The product {list(elem.keys())[0]} didnt save!!!')


class Command(BaseCommand):
    def handle(self, *args, **options):
        collect_number_of_products()
        