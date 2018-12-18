from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from .models import Events, Foods
from django.apps import apps
Groups = apps.get_model('groups_app', 'Groups')
Users = apps.get_model('login_app', 'Users')

def eventInfo(request, gid, eid):
    group=Groups.objects.get(id=gid)
    
    context = {
        'groupid' : gid,
        'thisevent' : Events.objects.get(id=eid),
        'userlist' : Users.objects.filter(groups__id=gid),
    }
    return render(request, 'event_info.html', context)
def addEvent(request, gid):
    context = {
        'groupid' : gid,
    }
    return render(request, 'add_event.html', context)
def createEvent(request, gid):
    errors = Events.objects.validateEvents(request.POST)
    if len(errors) > 0:
	    for key, value in errors.items():
		    messages.error(request, value)
		    return redirect(f'/group/{gid}/events/add')
    this_event = Events.objects.create(event_name=request.POST['eventname'], date=request.POST['eventdate'], time=request.POST['eventtime'], desc=request.POST['eventdesc'],groupid=Groups.objects.get(id=gid),created_by=Users.objects.get(id=request.session['id']))
    eid = this_event.id
    if 'hasfood' in request.POST:
        this_event.has_food = True
        this_event.save()
    return redirect(f'/group/{gid}/events/{eid}')
def editEvent(request, gid, eid):
    this_event = Events.objects.get(id=eid)
    date = this_event.date
    time = this_event.time
    context = {
        'groupid' : gid,
        'eventinfo' : Events.objects.get(id=eid),
        'eventdate' : str(date),
        'eventtime' : str(time),
    }
    return render(request, 'edit_event.html', context)
def updateEvent(request, gid, eid):
    errors = Events.objects.validateEvents(request.POST)
    if len(errors) > 0:
	    for key, value in errors.items():
		    messages.error(request, value)
		    return redirect(f'/group/{gid}/events/{eid}/edit')
    this_event = Events.objects.get(id=eid)
    this_event.event_name = request.POST['eventname']
    this_event.date = request.POST['eventdate']
    this_event.time = request.POST['eventtime']
    this_event.desc = request.POST['eventdesc']
    if 'hasfood' in request.POST:
        this_event.has_food = True
    if 'hasfood' not in request.POST:
        this_event.has_food = False
    this_event.save()
    return redirect(f'/group/{gid}/events/{eid}')
def deleteEvent(request, gid, eid):
    context = {
        'groupid' : gid,
    }
    return redirect(f"/group/{gid}", context)
def menu(request, gid, eid):
    context = {
        'groupid' : gid,
    }
    return render(request, 'menu.html', context)
def editMenu(request, gid, eid):
    context = {
        'groupid' : gid,
    }
    return render(request, 'editMenu.html', context)
def updateMenu(request, gid, eid):
    return redirect(f'/group/{gid}/events/{eid}/menu')
