from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from growth_project.apps.growth.models import *
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.template import RequestContext
from django.template import Context
from django.template.loader import get_template
import mysql.connector

def index(request):
    return render_to_response('landing_mvp.html', RequestContext(request) )
    #return render_to_response('growthmvp_clone1.html', RequestContext(request) )