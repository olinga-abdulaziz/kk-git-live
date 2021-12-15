from django.shortcuts import render
from django.views import generic
from . models import Post
from django.urls import reverse_lazy
# Create your views here.


class HomeView(generic.ListView):
    model=Post
    posts=Post.objects.all()
    context_object_name='posts'
    template_name = 'app1/home.html'
    ordering='-id'


class WeddingView(generic.ListView):
    model=Post
    ordering='-id'
    wedding=Post.objects.filter(category='wedding')
    context_object_name='wedding'
    template_name='app1/wedding.html'

class CommerciaView(generic.ListView):
    model=Post
    ordering='-id'
    commercia=Post.objects.filter(category='commercia')
    context_object_name='commercia'
    template_name='app1/commercia.html'

class CorporateView(generic.ListView):
    model=Post
    ordering='-id'
    corporate=Post.objects.filter(category='corporate')
    context_object_name='corporate'
    template_name='app1/corporate.html'

class EventsView(generic.ListView):
    model=Post
    ordering='-id'
    events=Post.objects.filter(category='events')
    context_object_name='events'
    template_name='app1/events.html'

class FasionView(generic.ListView):
    model=Post
    ordering='-id'
    fasion=Post.objects.filter(category='fasion')
    context_object_name='fasion'
    template_name='app1/fasion.html'

class PotraitsView(generic.ListView):
    model=Post
    ordering='-id'
    potrait=Post.objects.filter(category='potrait')
    context_object_name='potrait'
    template_name='app1/potraits.html'

class AddPostView(generic.CreateView):
    model=Post
    fields='__all__'
    template_name='app1/upload.html'
    success_url=reverse_lazy('home')


