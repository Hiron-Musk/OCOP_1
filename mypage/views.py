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

    qs_carbonpoint = Myuserpoint.objects.aggregate(Sum('carbonpoint'))
    sumcarbonpoint = qs_carbonpoint['carbonpoint__sum']

    qs_greenpoint = Myuserpoint.objects.aggregate(Sum('greenpoint'))
    sumgreenpoint = qs_greenpoint['greenpoint__sum']

    qs_vehiclepoint = Myuserpoint.objects.aggregate(Sum('vehiclepoint'))
    sumvehiclepoint = qs_vehiclepoint['vehiclepoint__sum']
    print(qs_carbonpoint)
    print(sumcarbonpoint)

    context = {'mypointcarbon_list': mypointcarbon_list, 'mypointgreen_list': mypointgreen_list, 'myuserpoint_list': myuserpoint_list,
               'sumcarbonpoint': sumcarbonpoint, 'sumgreenpoint':sumgreenpoint, 'sumvehiclepoint':sumvehiclepoint}
    return render(request, 'mypage/mypage.html', context)

def mypage_chart(request):
    data = []
    queryset = Myuserpoint.objects.all().aggregate(carbonpoint=Sum('carbonpoint'), greenpoint=Sum('greenpoint'), vehiclepoint=Sum('vehiclepoint'))
    print(queryset)

    values = queryset.values()
    valuelist = list(values)

    for entry in valuelist:
        data.append(entry)
        print(entry)

    return JsonResponse(data={'data':data})