from django.urls import path
from . import views

urlpatterns = [
    # localhost: 8000/trip -> views.dashboard
    path('', views.dashboard),
    # localhost: 8000/trip/new - views.new
    path('new', views.new),
    # localhost: 8000/trip/create
    path('create', views.create),
     #localhost: 8000/trip/<trip_id>/edit
    path('<int:trip_id>/edit', views.edit),
    #localhost: 8000/trip/<trip_id>/update
    path('<int:trip_id>/update', views.update),
    #localhost: 8000/trip/<trip_id>/check
    path('<int:trip_id>/check', views.check),
    #localhost: 8000/trip/delete
    path('<int:trip_id>/delete', views.delete)
]
