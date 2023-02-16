from django.core.management.base import BaseCommand

from services import collecting_scripts, secondary_scripts


class Command(BaseCommand):
    def handle(self, *args, **options):
        # collecting_scripts.collect_main_page_data()
        # collecting_scripts.collect_category_name_id()
        # collecting_scripts.collect_page_info()
        collecting_scripts.collect_product_info()
