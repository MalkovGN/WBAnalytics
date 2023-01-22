from django.core.management.base import BaseCommand

from wb_analytic_app.services import collect_all_urls, get_full_info_categories
from wb_analytic_app.models import CategoryPageInfo


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
        page_number = 1 # When I will know how many pages
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


class Command(BaseCommand):
    def handle(self, *args, **options):
        collect_page_info()
