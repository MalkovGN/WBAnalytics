from django.db import models


class ProductsNumberUrlsModel(models.Model):
    category = models.CharField(max_length=128)
    url = models.TextField()

    def __str__(self):
        return self.category


class ProductsInCategory(models.Model):
    category = models.CharField(max_length=128)
    counter = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Number of products in categories'

    def __str__(self):
        return self.category


class ProductsNotSaved(models.Model):
    category = models.CharField(max_length=128)
    url = models.TextField()

    class Meta:
        verbose_name_plural = 'Number of products urls not saved'

    def __str__(self):
        return self.category


class CategoryPageInfo(models.Model):
    name = models.CharField(max_length=128)
    wb_url = models.TextField()
    first_page_products_url = models.TextField()

    class Meta:
        verbose_name_plural = 'Category page infos'

    def __str__(self):
        return self.name
