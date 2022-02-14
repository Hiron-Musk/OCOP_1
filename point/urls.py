from django.urls import path
from . import views

app_name = "point"

urlpatterns = [
    path('createcarbon/', views.Createcarbon, name='createcarbon'),
    path('creategreen/', views.Creategreen, name='creategreen'),
    path('carbonlist/', views.Carbonlist, name='carbonlist'),
    path('greenlist/', views.Greenlist, name='greenlist'),
    path('carbonlist/modify/<int:Carbonpoint_id>/', views.Carbon_Modify, name='carbonmodify'),
    path('greenlist/modify/<int:Greenpoint_id>/', views.Green_Modify, name='greenmodify'),
    path('carbonlist/delete/<int:Carbonpoint_id>/', views.Carbon_Delete, name='carbondelete'),
    path('greenlist/delete/<int:Greenpoint_id>/', views.Green_Delete, name='greendelete'),



    path('carbon/', views.Carbonpage, name='carbonpage'),
    path('green/', views.Greenpage, name='greenpage'),
    path('detail/', views.Detail, name='detail'),
    path('detailgreen/', views.Detailgreen, name='detailgreen'),
    path('add/<int:Carbonpoint_id>/', views.Add, name='add'),
    path('addgreen/<int:Greenpoint_id>/', views.Addgreen, name='addgreen'),
    path('remove/<int:Carbonpoint_id>/',views.Remove, name='remove'),
    # path('removecarbon/', views.Removecarbon, name='removecarbon'),
    path('removegreen/<int:Greenpoint_id>/', views.Removegreen, name='removegreen'),
    path('saveusercarbon/', views.Saveusercarbon, name='saveusercarbon'),
    path('usercarbon/', views.Usercarbon, name='usercarbon'),
    path('saveusergreen/', views.Saveusergreen, name='saveusergreen'),
]