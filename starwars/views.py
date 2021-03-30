from django.shortcuts import render
from .models import History, PeopleImage
from django.utils import timezone
import requests
from django.http import HttpResponseServerError
from django.conf import settings

def home(request):
    History.objects.create(url=request.build_absolute_uri(), date=timezone.now())
    r = requests.get(settings.BASE_URL + 'people')
    peoples = r.json().get('results')
    names = []
    for people in peoples:
        people_image = PeopleImage.objects.filter(peoples__contains=people.get('name'))
        if not people_image:
            image_url = settings.IMAGE_URL + people.get('name').replace(' ', '+')
        else:
            image_url = people_image[0].image.url
        names.append((image_url, people.get('name')))
    if r.status_code == 200:
        return render(request, 'starwars/index.html', {'peoples': names})
    return HttpResponseServerError()

def film(request):
    History.objects.create(url=request.build_absolute_uri(), date=timezone.now())
    text = request.GET['search_text']
    films = search(text, 'films')
    return render(request, 'starwars/film.html', {'films': films})

def history(request):
    History.objects.create(url=request.build_absolute_uri(), date=timezone.now())
    historys = History.objects.all()
    return render(request, 'starwars/history.html', {'historys': historys})

def search(text, type):
    r = requests.get(settings.BASE_URL + type + '/?search=' + text)
    results = r.json().get('results')
    return results