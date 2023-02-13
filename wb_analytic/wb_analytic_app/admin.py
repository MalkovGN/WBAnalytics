from django.contrib import admin

from . import models

admin.site.register(models.ProductsNumberUrlsModel)

admin.site.register(models.ProductsInCategory)

admin.site.register(models.ProductsNotSaved)

admin.site.register(models.CategoryPageInfo)

admin.site.register(models.ProductInfo)

admin.site.register(models.CategoriesNotSaved)

admin.site.register(models.AmountProductsNotSaved)

admin.site.register(models.AnalyticCategoryModel)

admin.site.register(models.CategoryNameModel)
