from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users
import bcrypt

def index(request):
	return render(request, 'login_app/index.html')

def login(request):
	print("logged in")
	user = Users.objects.filter(user_name=request.POST['username'].lower())
	errors = Users.objects.login_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	request.session['id'] = user[0].id
	request.session['name'] = user[0].first_name
	return redirect('/home')








def signup(request):
	return render(request, 'login_app/signup.html')

def register(request):
	errors = Users.objects.validate(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/signup')
	else:
		hash1 = bcrypt.hashpw(request.POST['password1'].encode(), bcrypt.gensalt())
		Users.objects.create(user_name=request.POST['username'], first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'].lower(), password=hash1.decode())
		request.session['id'] = Users.objects.last().id
		request.session['name'] = Users.objects.last().first_name
		return redirect('/home')

def home(request):
	if 'id' in request.session:
		return render(request, 'login_app/home.html')
	else:
		return redirect('/')


def logout(request):
	request.session.flush()
	return redirect('/')