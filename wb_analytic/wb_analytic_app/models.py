from django.db import models


class ProductsNumberUrlsModel(models.Model):
    category = models.CharField(max_length=128)
    url = models.TextField()

    def __str__(self):
        return self.category
