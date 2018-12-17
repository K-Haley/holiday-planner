from django.shortcuts import render

def groupInfo(request, gid):
    return render(request, 'group_info.html')
def editGroup(request, gid):
    return render(request, 'edit_group.html')
def groupOneUser(request, gid, uid):
    return render(request, 'group_one_user.html')