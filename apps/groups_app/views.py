from django.shortcuts import render, redirect
from .models import Groups
from django.apps import apps
from django.contrib import messages
Users = apps.get_model('login_app', 'Users')
Events = apps.get_model('events_app', 'Events')
Items = apps.get_model('login_app', 'Items')

def groupInfo(request, gid): 
    this_group = Groups.objects.get(id=gid)
    owner = this_group.group_owner
    group_name = this_group.group_name
    request.session['group_name'] =group_name
    groupname = ''
    for i in range(0, len(group_name)):
        if group_name[i] != ' ':
            groupname += group_name[i]
    print(groupname)
    context = {
        'userlist' : Users.objects.filter(groups__id=gid),
        'groupowner' : owner.id,
        'description' : this_group.group_desc,
        'eventlist' : Events.objects.filter(groupid__id=gid),
        'groupid' : gid,
        'group_name': group_name,
        'groupname' : groupname,
    }
    return render(request, 'group_info.html', context)
def editGroup(request, gid):
    this_group = Groups.objects.get(id=gid)
    owner = this_group.group_owner
    group_name = this_group.group_name
    context = {
        'userlist' : Users.objects.filter(groups__id=gid),
        'groupowner' : owner.id,
        'eventlist' : Events.objects.filter(groupid__id=gid),
        'groupid' : gid,
        'group_name': group_name,
    }
    return render(request, 'edit_group.html', context)
def removeUser(request, gid, uid):
    this_group = Groups.objects.get(id=gid)
    this_user = Users.objects.get(id=uid)
    this_group.members.remove(this_user)
    return redirect(f'/group/{gid}/edit')
def groupInvite(request, gid):
    this_group = Groups.objects.get(id=gid)
    this_user = Users.objects.get(user_name=request.POST['inviteuser'])
    this_group.members.add(this_user)
    print(this_group.members)
    return redirect(f'/group/{gid}')
def groupOneUser(request, gid, uid):
    context = {
        'this_user' : Users.objects.get(id=uid),
        'wishlist' : Items.objects.filter(userid__id=uid),
        'userid' : uid,
        'groupid' : gid,
    }
    return render(request, 'group_one_user.html', context)
def take(request, gid, uid, iid):
    this_item = Items.objects.get(id=iid)
    this_item.taken = True
    this_item.save()
    return redirect(f'/group/{gid}/{uid}')
def addGroup(request):
    return render(request, 'add_group.html')
def createGroup(request):
    errors = Groups.objects.validateGroups(request.POST)
    if len(errors) > 0:
	    for key, value in errors.items():
		    messages.error(request, value)
		    return redirect('/group/add')
    this_group = Groups.objects.create(group_name=request.POST['groupname'], group_desc=request.POST['groupdesc'],group_owner=Users.objects.get(id=request.session['id']))
    this_group.members.add(Users.objects.get(id=request.session['id']))
    return redirect(f"/group/{this_group.id}/")
def deleteGroup(request, gid):
    this_group = Groups.objects.get(id=gid)
    this_group.delete()
    return redirect('/home')