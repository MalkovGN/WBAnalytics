# Generated by Django 4.0.6 on 2023-01-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wb_analytic_app', '0004_categorypageinfo_alter_productsincategory_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('feedbacks', models.IntegerField()),
                ('sale_price', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Products info',
            },
        ),
        migrations.AlterModelOptions(
            name='categorypageinfo',
            options={'verbose_name_plural': 'All category page infos'},
        ),
    ]