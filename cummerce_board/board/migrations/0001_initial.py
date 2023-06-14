# Generated by Django 3.2.5 on 2023-06-14 05:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.TextField(verbose_name='상품명')),
                ('thumb_img', models.TextField(verbose_name='모델이미지')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('detail_img', models.TextField(verbose_name='상세페이지이미지')),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_id', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3, '올바른 이름을 입력해주세요.')], verbose_name='작성자')),
                ('content', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3, '최소 세 글자 이상은 입력해주셔야 합니다.')], verbose_name='댓글')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.item')),
            ],
        ),
    ]
