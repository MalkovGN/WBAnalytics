from django.contrib import admin

from .models import ProductsNumberUrlsModel, ProductsInCategory, ProductsNotSaved, CategoryPageInfo


admin.site.register(ProductsNumberUrlsModel)

admin.site.register(ProductsInCategory)

admin.site.register(ProductsNotSaved)

admin.site.register(CategoryPageInfo)