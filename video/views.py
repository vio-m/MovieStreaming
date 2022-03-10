from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Video, Genre


def all(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'all.html', context)


@login_required(login_url='login')
def detail(request, pk):
    video = Video.objects.get(id=pk)
    context = {'video': video}
    return render(request, 'detail.html', context)


def search(request):
    q = request.GET.get('q')
    lookups = Q(title__icontains=q) | Q(year__icontains=q)
    results = Video.objects.filter(lookups)
    context = {"videos": results}
    return render(request, 'results.html', context)


def get_genre(request):
    genres = Genre.objects.all()
    context = {'genres': genres}
    return context


def genres(request, pk):
    videos = Video.objects.filter(genre=pk)
    context = {'videos': videos}
    return render(request, 'genres.html', context)