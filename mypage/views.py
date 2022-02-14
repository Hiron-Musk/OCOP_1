import base64
import io
import urllib.parse
import matplotlib.pyplot as plt
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from datetime import datetime
from .models import Mypointcarbon, Mypointgreen, Myuserpoint
from django.db.models import Sum


def mypage(request):
    mypointcarbon_list = Mypointcarbon.objects.all()
    mypointgreen_list = Mypointgreen.objects.all()
    myuserpoint_list = Myuserpoint.objects.all()
    context = {'mypointcarbon_list': mypointcarbon_list, 'mypointgreen_list': mypointgreen_list, 'myuserpoint_list': myuserpoint_list}
    return render(request, 'mypage/mypage.html', context)

def mypage_chart(request):
    data = []
    queryset = Myuserpoint.objects.values('carbonpoint', 'greenpoint','vehiclepoint')
    print(queryset)

    for entry in queryset:
        data.append(entry['carbonpoint'])
        data.append(entry['greenpoint'])
        data.append(entry['vehiclepoint'])
        print(data)

    return JsonResponse(data={
        'data':data
    })
