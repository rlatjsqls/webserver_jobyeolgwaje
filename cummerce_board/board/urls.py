from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board_item, name='board_item'),
    path('<int:item_id>', views.board_detail, name='detail'),
    # path('detail/', views.bo, name='ddetail')
    path('wordcloud/<int:item_id>/',
         views.review_wordcloud, name='review_wordcloud'),
]
