# Generated by Django 3.2.5 on 2023-06-16 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_remove_comment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category_id',
            field=models.IntegerField(default=0, verbose_name='카테고리ID'),
        ),
    ]
