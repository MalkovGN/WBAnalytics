from django.contrib import admin

from .models import ProductsNumberUrlsModel, ProductsInCategory, ProductsNotSaved


admin.site.register(ProductsNumberUrlsModel)

admin.site.register(ProductsInCategory)

admin.site.register(ProductsNotSaved)