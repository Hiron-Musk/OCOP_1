import base64
import io
import urllib.parse

from django.shortcuts import render, get_object_or_404, redirect
import matplotlib.pyplot as plt

# Create your views here.

def mypage(request):
    plt.plot([10, 20, 30, 40, 50, 60, 70], [1, 4, 9, 16, 20, 25, 40], 'rs--')
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'mypage/mypage.html', {'data':uri})
