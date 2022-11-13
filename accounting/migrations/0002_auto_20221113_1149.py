# Generated by Django 4.1.3 on 2022-11-13 08:49

from django.db import migrations
from accounting.models import DEFAULT_CATEGORIES, Category


def fill_default_categories(app, schema):
    for category in DEFAULT_CATEGORIES:
        new_category = Category(category=category)
        new_category.save()


class Migration(migrations.Migration):

    dependencies = [
        ("accounting", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(fill_default_categories),
    ]