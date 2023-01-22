from django.contrib import admin

from .models import ProductsNumberUrlsModel, ProductsInCategory, ProductsNotSaved, CategoryPageInfo, ProductInfo, CategoriesNotSaved


admin.site.register(ProductsNumberUrlsModel)

admin.site.register(ProductsInCategory)

admin.site.register(ProductsNotSaved)

admin.site.register(CategoryPageInfo)

admin.site.register(ProductInfo)

admin.site.register(CategoriesNotSaved)
