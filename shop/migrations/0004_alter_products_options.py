# Generated by Django 3.2.8 on 2021-10-19 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_categ_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('name',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]
