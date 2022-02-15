from django.urls import path
# from .views import MyView
    # , MypointView
from . import views

app_name = 'mypage'

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('mypage-chart/', views.mypage_chart, name='mypage-chart'),
]