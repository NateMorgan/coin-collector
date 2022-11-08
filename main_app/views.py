from django.shortcuts import render, redirect
from .models import Collection, Coin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from .forms import OfferForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def collections_index(request):
  collections = Collection.objects.all()
  return render(request, 'collections/index.html', {'collections': collections})

def collections_detail(request,collection_id):
  collection = Collection.objects.get(id=collection_id)
  offer_form = OfferForm()
  return render(request, 'collections/detail.html', {'collection': collection, 'offer_form':offer_form})


def add_offer(request, collection_id):
  form = OfferForm(request.POST)
  if form.is_valid():
    new_offer = form.save(commit=False)
    new_offer.collection_id = collection_id
    new_offer.save()
  return redirect('collections_detail', collection_id=collection_id)


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

class CoinCreate(CreateView):
  model = Coin
  fields = '__all__'
  
class CoinList(ListView):
  model = Coin

class CoinDetail(DetailView):
  model = Coin

class CoinUpdate(UpdateView):
  model = Coin
  fields = ['name', 'mintage', 'image']

class CoinDelete(DeleteView):
  model = Coin
  success_url = '/coins/'