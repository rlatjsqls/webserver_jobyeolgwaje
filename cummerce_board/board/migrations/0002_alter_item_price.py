# Generated by Django 3.2.5 on 2023-06-14 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.CharField(max_length=225, verbose_name='가격'),
        ),
    ]
