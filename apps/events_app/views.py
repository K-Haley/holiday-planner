from django.shortcuts import render, redirect

def eventInfo(request, gid, eid):
    return render(request, 'event_info.html')
def addEvent(request, gid):
    return render(request, 'add_event.html')
def editEvent(request, gid, eid):
    return render(request, 'edit_event.html')
def deleteEvent(request, gid, eid):
    return redirect(f"/group/{gid}")