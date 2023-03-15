from django.contrib import admin

from . import models


class Admin(admin.ModelAdmin):
    readonly_fields = ('save_date',)


admin.site.register(models.ProductsNumberUrlsModel)

admin.site.register(models.ProductsInCategory)

admin.site.register(models.ProductsNotSaved)

admin.site.register(models.CategoryPageInfo)

admin.site.register(models.ProductInfo, Admin)

admin.site.register(models.CategoriesNotSaved)

admin.site.register(models.AmountProductsNotSaved)

admin.site.register(models.AnalyticCategoryModel)

admin.site.register(models.CategoryNameModel)
