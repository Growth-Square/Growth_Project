from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from growth_project.apps.main.models import *
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.template import RequestContext
from django.template import Context
from django.template.loader import get_template
from growth_project.apps.main.models import Template as templates
import mysql.connector


def index(request):
    return render_to_response('landing_mvp.html', RequestContext(request))


def dashboard(request):
    return render_to_response('dashboard.html', {'user': request.user})


def selector(request):
    conn = mysql.connector.connect(user='root', database='growthdb')
    cursor = conn.cursor()

    try:
        # inventory_data = inventory.objets.get(hostname=hostname)
        templates_data = templates.objects.all()
        return render(request, 'selector_landing.html',
                                  {'user': request.user, 'templates': templates_data})
    except templates.DoesNotExist:
        return render(request, 'selector_landing.html',
                                  {'user': request.user, 'error_message': "No hay templates ingresados"})
        # return HttpResponseRedirect('/accounts/invalid_login'


"""
    cursor.execute("SELECT * FROM main_template")
    rows = cursor.fetchall()
    t = Context({'results': rows})

    return render_to_response('selector_landing.html', t)
    """
