from django.core.management.base import BaseCommand

from wb_analytic_app.services import retry_saving_sold_numbers


class Command(BaseCommand):
    def handle(self, *args, **options):
        retry_saving_sold_numbers()
