from django.urls import path
from . import views

urlpatterns = [
    path('<int:gid>', views.groupInfo),
    path('<int:gid>/edit', views.editGroup),
    path('<int:gid>/<int:uid>', views.groupOneUser),
    
]