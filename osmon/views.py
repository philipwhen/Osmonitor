from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
import os


def index(request):
    kernelversion = os.popen("uname -a").read()
    datetime = os.popen("date").read()
    ip = os.popen("curl -s ipecho.net/plain").read()
    template = loader.get_template('osmon/index.html')
    context = {
        'kernelversion': kernelversion,    
        'datetime': datetime,
        'ip': ip,
    }
    return HttpResponse(template.render(context,request))