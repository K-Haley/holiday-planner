from django.urls import path
from . import views

urlpatterns = [
    path('<int:eid>', views.eventInfo),
    path('add', views.addEvent),
    path('<int:eid>/edit', views.editEvent),
]