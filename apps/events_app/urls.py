from django.urls import path
from . import views

urlpatterns = [
    path('<int:eid>', views.eventInfo),
    path('<int:eid>/menu', views.menu),
    path('<int:eid>/menu/edit', views.editMenu),
    path('<int:eid>/menu/add', views.addToMenu),
    path('<int:eid>/menu/<int:fid>/delete', views.updateMenu),
    path('add', views.addEvent),
    path('create', views.createEvent),
    path('<int:eid>/edit', views.editEvent),
    path('<int:eid>/update', views.updateEvent),
    path('<int:eid>/delete', views.deleteEvent),
]