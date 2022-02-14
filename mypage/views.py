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
from .models import Mypointcarbon, Mypointgreen
    # Userpoint
from django.db.models import Sum


def mypage(request):
    mypointcarbon_list = Mypointcarbon.objects.all()
    mypointgreen_list = Mypointgreen.objects.all()
    # myuserpoint_list = Userpoint.objects.all()
    context = {'mypointcarbon_list': mypointcarbon_list, 'mypointgreen_list': mypointgreen_list, }
    # 'myuserpoint_list': myuserpoint_list,
    return render(request, 'mypage/mypage.html', context)

def mypage_chart(request):

    # point_list = list(Userpoint.objects.all())
    # print(point_list)

    labels = []
    data = []
    queryset = Mypointcarbon.objects.values('pointtype').annotate(cpoint=Sum('cpoint')).order_by('-cpoint')
    for entry in queryset:
        labels.append(entry['pointtype'])
        data.append(entry['cpoint'])

    return JsonResponse(data={
        # 'point_list': point_list,
        'labels':labels,
        'data':data,
    })
