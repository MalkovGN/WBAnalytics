import random
import requests
import time

from django.core.management.base import BaseCommand

from wb_analytic_app.models import ProductsNotSaved, ProductsInCategory


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


def retry_sending_requests():
    not_saved_objects = ProductsNotSaved.objects.all()
    for elem in not_saved_objects:
        url = elem.url
        prox = random.choice(proxies)

        try:
            response = requests.get(url, proxies=prox)
            time.sleep(random.choice(times_sleeps))
            product_in_category = ProductsInCategory(
                category=elem.category,
                counter=response.json()['data']['total'],
            )
            product_in_category.save()
            ProductsNotSaved.objects.filter(id=elem.id).delete()
            print(f'The product {elem.category} saved successfully!')
        except Exception:
            print(f'The product {elem.category} didnt saved!!!')


class Command(BaseCommand):
    def handle(self, *args, **options):
        retry_sending_requests()
