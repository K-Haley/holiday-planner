from django.shortcuts import render, redirect
from .models import Groups
from django.apps import apps
Users = apps.get_model('login_app', 'Users')
Events = apps.get_model('events_app', 'Events')
Items = apps.get_model('login_app', 'Items')

def groupInfo(request, gid):
    context = {
        'userlist' : Users.objects.filter(groups__id=gid),
        'eventlist' : Events.objects.filter(groupid__id=gid),
        'groupid' : gid,
    }
    return render(request, 'group_info.html', context)
def editGroup(request, gid):
    context = {
        'userlist' : Users.objects.filter(groups__id=gid),
        'eventlist' : Events.objects.filter(groupid__id=gid),
        'groupid' : gid,
    }
    return render(request, 'edit_group.html', context)
def removeUser(request, gid, uid):
    this_group = Groups.objects.get(id=gid)
    this_user = Users.objects.get(id=uid)
    this_group.Users.remove(this_user)
    return redirect(f'/{gid}/edit')
def groupOneUser(request, gid, uid):
    context = {
        'this_user' : Users.objects.get(id=uid),
        'wishlist' : Items.objects.filter(userid__id=uid)
    }
    return render(request, 'group_one_user.html', context)