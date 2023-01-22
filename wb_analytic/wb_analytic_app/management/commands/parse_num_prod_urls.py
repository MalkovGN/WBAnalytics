import random
import requests
import time

from django.core.management.base import BaseCommand

from wb_analytic_app.services import collect_all_urls, get_full_info_categories, number_of_products_links, get_categories_without_shard
from wb_analytic_app.models import ProductsNumberUrlsModel, ProductsInCategory, ProductsNotSaved


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


def save_to_db_num_prod():
    """
    Saving to db link which have
    a number of products in category
    """
    subcategories_info = collect_all_urls()
    s1 = get_full_info_categories(subcategories_info)
    s2 = number_of_products_links(s1)

    for subcategory in s2:
        subcategory_info = ProductsNumberUrlsModel(
            category=list(subcategory.keys())[0],
            url=list(subcategory.values())[0],
        )
        subcategory_info.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        save_to_db_num_prod()
