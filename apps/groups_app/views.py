from django.shortcuts import render

def groupList(request):
    return render(request, 'group_list.html')
def groupInfo(request, gid):
    return render(request, 'group_info.html')
def groupUser(request, gid):
    return render(request, 'group_users.html')
def groupOneUser(request, gid, uid):
    return render(request, 'group_one_user.html')