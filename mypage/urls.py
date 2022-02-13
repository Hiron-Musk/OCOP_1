from django.urls import path
# from .views import MyView
    # , MypointView
from . import views

app_name = 'mypage'

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('mypage-chart/', views.mypage_chart, name='mypage-chart'),
    # path('', MyView.as_view(), name='my-view'),
    # path('', MypointView.as_view(), name='my-point-view'),
    # path('<int:mypage_carbon_id>/', views.mypage, name='mypage'),
]