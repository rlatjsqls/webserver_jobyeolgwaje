from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board_item, name='board_item'),
    path('<int:item_id>', views.board_detail, name='detail'),
    # path('detail/', views.bo, name='ddetail')
    path('category/<int:category_id>', views.board_category, name='category'),
    path('wordcloud/<int:item_id>/',
         views.review_wordcloud, name='review_wordcloud'),
    path('api/wordcloud/<int:item_id>/',
         views.review_dynamic, name='review_wordcloud'),
]
# {% url 'board:category' category_id = 200001481 %}
# 찾기
