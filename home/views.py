from django.shortcuts import render
from chat.models import *

# Create your views here.

def home(request):
	chat = ChatMessage.objects.all()
	return render(request,'common/home.html', {'chat':chat})

def video(request):
	return render(request,'video.html')

def video3(request):
	return render(request,'video3.html')

def video5(request):
	return render(request,'video5.html')

def video6(request):
	return render(request,'video6.html')

def call(request):
	return render(request,'final.html')

def room_selection(request):
	return render(request, 'room_selection.html')

def room(request, room_name):
	user_name = request.GET.get('user', 'Anonymous')
	return render(request, 'room.html', {
		'room_name': room_name,
		'user_name': user_name
	})
