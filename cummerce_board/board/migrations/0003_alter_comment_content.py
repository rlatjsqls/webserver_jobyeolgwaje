# Generated by Django 3.2.5 on 2023-06-14 09:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(3, '최소 세 글자 이상은 입력해주셔야 합니다.')], verbose_name='댓글'),
        ),
    ]
