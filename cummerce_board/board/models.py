from django.core import validators
from django.utils import timezone
from django.db import models

# Create your models here.


class Item(models.Model):
    id = models.AutoField(primary_key=True)  # 아이템에 대한 pk
    product_name = models.TextField('상품명')
    thumb_img = models.TextField('모델이미지')
    price = models.IntegerField('가격')
    detail_img = models.TextField('상세페이지이미지')
    is_deleted = models.BooleanField(default=False)


class Comment(models.Model):
    reviewer_id = models.CharField('작성자', max_length=255,
                                   validators=[
                                       validators.MinLengthValidator(
                                           3, "올바른 이름을 입력해주세요."
                                       )
                                   ])
    content = models.CharField("댓글", max_length=255,
                               validators=[
                                   validators.MinLengthValidator(
                                       3, "최소 세 글자 이상은 입력해주셔야 합니다."
                                   )
                               ])
    created_at = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey('Item',
                             # related_name='comment_set',
                             on_delete=models.SET_NULL, null=True)
