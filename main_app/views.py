from django.shortcuts import render
from .models import Collection
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def collections_index(request):
  collections = Collection.objects.all()
  return render(request, 'collections/index.html', {'collections': collections})

def collections_detail(request,collection_id):
  collection = Collection.objects.get(id=collection_id)
  return render(request, 'collections/detail.html', {'collection': collection})

class CollectionCreate(CreateView):
  model = Collection
  fields = '__all__'
  success_url = '/collections/'

class CollectionUpdate(UpdateView):
  model = Collection
  fields = ['name', 'description']

class CollectionDelete(DeleteView):
  model = Collection
  success_url = '/collections/'