from django.shortcuts import render

def events(request, gid):
    return render(request, 'event_list.html')
def eventInfo(request, gid, eid):
    return render(request, 'event_info.html')
def addEvent(request, gid):
    return render(request, 'add_event.html')
def editEvent(request, gid, eid):
    return render(request, 'edit_event.html')