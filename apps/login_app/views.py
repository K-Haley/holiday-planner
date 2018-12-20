from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users, Items
import bcrypt
from datetime import datetime, timezone, timedelta
from django.apps import apps
Groups = apps.get_model('groups_app', 'Groups')
Events = apps.get_model('events_app', 'Events')
PMessages = apps.get_model('groups_app', 'PMessages')

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
		mylist = Items.objects.filter(userid=request.session['id'])
		print(Groups.objects.all().values())
		mygroups = Groups.objects.filter(members=request.session['id'])
		print(mygroups)
		myevents = Events.objects.filter(groupid__members=Users.objects.get(id=request.session['id']))
		mymessages = PMessages.objects.filter(sent_to=Users.objects.get(id=request.session['id'])).order_by('-created_at')
		sentmessages = PMessages.objects.filter(posted_by=Users.objects.get(id=request.session['id'])).order_by('-created_at')
		timeSinceMy = []
		for i in mymessages:
			j = datetime.now(timezone.utc) - i.created_at
			if j.days > .99999999:
				j = f'{round(j.days)} days(s)'
			elif j.seconds/3600 > 1:
				j = f'{round(j.seconds/3600)} hour(s)'
			else:
				j = f'{round(j.seconds/60)} minute(s)'
			timeSinceMy.append(j)
		timeSinceSent = []
		for x in sentmessages:
			y = datetime.now(timezone.utc) - x.created_at
			if y.days > .99999999:
				y = f'{round(y.days)} days(s)'
			elif y.seconds/3600 > 1:
				y = f'{round(y.seconds/3600)} hour(s)'
			else:
				y = f'{round(y.seconds/60)} minute(s)'
			timeSinceSent.append(y)
		my_messages = zip(mymessages,timeSinceMy)
		sent_messages = zip(sentmessages,timeSinceSent)
		print("*********************************************************")
		print(my_messages)
		context={
			"mylist": mylist,
			"mygroups": mygroups,
			"myevents": myevents,
			"mymessages" : my_messages,
			"sentmessages" : sent_messages,
		}
		return render(request, 'login_app/home.html', context)
	else:
		return redirect('/')



def mylist(request):
	mylist = Items.objects.filter(userid=request.session['id'])
	context={
		"mylist": mylist
	}
	return render(request, 'login_app/mylist.html', context)

def add(request):
	Items.objects.create(item=request.POST['item'], userid=Users.objects.get(id=request.POST['userid']))
	return redirect('/mylist')

def delete(request, itemid):
	Items.objects.get(id=itemid).delete()
	return redirect('/mylist')




def logout(request):
	request.session.flush()
	return redirect('/')