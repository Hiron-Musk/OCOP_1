from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'OCOP'

urlpatterns = [
    path('',views.main_page,name='OCOP'),
    path('login/',auth_views.LoginView.as_view(template_name='OCOP/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.signup,name='signup'),
]