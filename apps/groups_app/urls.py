from django.urls import path
from . import views

urlpatterns = [
    path('', views.groupList),
    path('<int:gid>', views.groupInfo),
    path('<int:gid>/users', views.groupUser),
    path('<int:gid>/<int:uid>', views.groupOneUser),
]