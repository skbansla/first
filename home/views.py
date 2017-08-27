from django.shortcuts import render
from django.http import HttpResponse
from .models import Song

# Create your views here.
def home(request):
    song_list = Song.objects.all() #to get all data from db to song_list
    data_for_page = {'songs':song_list} #to send data to page
    
    return render(request, 'home.html',data_for_page) #render all 
