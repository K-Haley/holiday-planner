from django.shortcuts import render
import datetime
from django.apps import apps
Events = apps.get_model('events_app', 'Events')
Users = apps.get_model('login_app', 'Users')

def Calendar(request, uid):
    now = datetime.date.today()
    mydates = []
    weekdays = []
    oneday = datetime.timedelta(days=1)
    for _ in range(30):
        mydates.append(now)
        weekdays.append(now.weekday())
        now += oneday
    datesAndDays = { 'datedays': zip(mydates, weekdays) }
    today = weekdays[0]
    reset = []
    count = [1]
    for _ in range(weekdays[0]):
        count.append(1)
    if len(count) == 7:
        count = reset
    myevents = Events.objects.filter(groupid__members=Users.objects.get(id=request.session['id']))
    context = {
        'dates' : datesAndDays,
        'thisday' : today,
        'iterations' : count,
        'myevents' : myevents,
    }
    return render(request, 'calendar.html', context)