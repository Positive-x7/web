from django.shortcuts import render
from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><h1>It is now %s.</h1></html>' % now
    return HttpResponse(html)

def index(request):
    return render(request , "blog/index.html", {})

def cat(request, catid):
    return HttpResponse(f"<h1>Cats {catid} </h1>")