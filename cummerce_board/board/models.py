from django.core import validators
from django.utils import timezone
from django.db import models

# Create your models here.


class Comment(models.Model):
    reviewer_id = models.CharField('작성자', max_length=255,
                                   validators=[
                                       validators.MinLengthValidator(
                                           3, "올바른 이름을 입력해주세요."
                                       )
                                   ])
    content = models.TextField("댓글",
                               validators=[
                                   validators.MinLengthValidator(
                                       3, "최소 세 글자 이상은 입력해주셔야 합니다."
                                   )
                               ])
    item = models.ForeignKey('Item',
                             # related_name='comment_set',
                             on_delete=models.SET_NULL, null=True)


class Item(models.Model):
    id = models.AutoField(primary_key=True)  # 아이템에 대한 pk
    category_id = models.IntegerField('카테고리ID', default=0)
    product_name = models.TextField('상품명')
    thumb_img = models.TextField('모델이미지')
    price = models.CharField('가격', max_length=225)
    detail_img = models.TextField('상세페이지이미지')
    is_deleted = models.BooleanField(default=False)
