from django.shortcuts import render

def Calendar(request):
    return render(request, 'calendar.html')