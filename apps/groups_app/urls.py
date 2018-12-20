from django.urls import path
from . import views

urlpatterns = [
    path('<int:gid>/', views.groupInfo),
    path('<int:gid>/invite', views.groupInvite),
    path('add/', views.addGroup),
    path('<int:gid>/delete', views.deleteGroup),
    path('create/', views.createGroup),
    path('<int:gid>/edit/', views.editGroup),
    path('<int:gid>/<int:uid>/', views.groupOneUser),
    path('<int:gid>/<int:uid>/take/<int:iid>', views.take),
    path('<int:gid>/<int:uid>/remove/', views.removeUser),
    path('search', views.searchUsers),
]