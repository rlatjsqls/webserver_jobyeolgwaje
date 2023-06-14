from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:item_id>', views.board_detail, name='detail'),
    path('detail/', views.detail, name='ddetail')
]
