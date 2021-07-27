from django.shortcuts import render, HttpResponse
from movie.models import add_movie
# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_movie(request):
    if request.method== "POST":
        movie_name = request.POST.get('movie_name')
        Add_movie = add_movie(movie_name=movie_name)
        Add_movie.save()
    return render(request, 'add_movie.html')

def show_movie(request):
    return render(request, 'show_movie.html')