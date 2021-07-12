from django.shortcuts import render, redirect
from .models import Trip
from login.models import User
#from django.contrib import messages

# Create your views here.
def dashboard(request):
    context = {
        "trips" : Trip.objects.all(),
        "user" : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'trip/dashboard.html', context)

def new(request):
    context = {
        "user" : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'trip/new.html', context)

def create(request):
    #errors = Trip.objects.validate(request.POST)
    #if errors:
     #   for err in errors.values():
      #      messages.error(request, err)

       #     return redirect('/trip/new')

    Trip.objects.create(
        destination=request.POST['destination'],
        start_date=request.POST['start_date'],
        end_date=request.POST['end_date'],
        plan=request.POST['plan'],
        planner=User.objects.get(id=request.session['user_id'])
    )
    return redirect('/trip')

def edit(request, trip_id):
    context = {
        "trip" : Trip.objects.get(id=trip_id)
    }
    return render(request, 'trip/edit.html', context)

def update(request, trip_id):
    to_update = Trip.objects.get(id=trip_id)
    to_update.destination = request.POST['destination'],
    to_update.start_date = request.POST['start_date'],
    to_update.end_date = request.POST['end_date'],
    to_update.plan = request.POST['plan'],
    to_update.save()

    return redirect('/trip')

def check(request, trip_id):
    context = {
        "trip" : Trip.objects.get(id=trip_id)
    }
    return render(request, 'trip/check.html', context)

def delete(request, trip_id):
    to_delete = Trip.objects.get(id=trip_id)
    to_delete.delete()

    return redirect('/trip')