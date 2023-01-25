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
        verbose_name_plural = 'All category page infos'

    def __str__(self):
        return self.name


class CategoriesNotSaved(models.Model):
    name = models.CharField(max_length=128)
    wb_url = models.TextField()
    first_page_products_url = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories not saved'

    def __str__(self):
        return self.name


class ProductInfo(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=255)
    feedbacks = models.IntegerField()
    sale_price = models.IntegerField()
    price = models.IntegerField()
    sold_number = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(CategoryPageInfo, on_delete=models.CASCADE)
    save_date = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products info'

    def __str__(self):
        return self.name


class AmountProductsNotSaved(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryPageInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Amount sold products not saved'

    def __str__(self):
        return self.name
