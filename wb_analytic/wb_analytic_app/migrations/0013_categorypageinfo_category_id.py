# Generated by Django 4.0.6 on 2023-02-13 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wb_analytic_app', '0012_categorynamemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorypageinfo',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wb_analytic_app.categorynamemodel'),
        ),
    ]