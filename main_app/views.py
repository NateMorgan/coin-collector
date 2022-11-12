from django.shortcuts import render, redirect
from .models import Collection, Coin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from .forms import OfferForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def collections_index(request):
  collections = Collection.objects.filter(user=request.user)
  return render(request, 'collections/index.html', {'collections': collections})

@login_required
def collections_detail(request,collection_id):
  collection = Collection.objects.get(id=collection_id)
  coins_collection_doesnt_have = Coin.objects.exclude(id__in = collection.coins.all().values_list('id'))
  offer_form = OfferForm()
  return render(request, 'collections/detail.html', {'collection': collection, 'offer_form':offer_form, 'coins': coins_collection_doesnt_have})

@login_required
def add_offer(request, collection_id):
  form = OfferForm(request.POST)
  if form.is_valid():
    new_offer = form.save(commit=False)
    new_offer.collection_id = collection_id
    new_offer.save()
  return redirect('collections_detail', collection_id=collection_id)

@login_required
def assoc_coin(request,collection_id, coin_id):
  Collection.objects.get(id=collection_id).coins.add(coin_id)
  return redirect('collections_detail', collection_id=collection_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('collections_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class CollectionCreate(LoginRequiredMixin, CreateView):
  model = Collection
  fields = ['name', 'description']
  success_url = '/collections/'

class CollectionUpdate(LoginRequiredMixin, UpdateView):
  model = Collection
  fields = ['name', 'description']

class CollectionDelete(LoginRequiredMixin, DeleteView):
  model = Collection
  success_url = '/collections/'

class CoinCreate(LoginRequiredMixin, CreateView):
  model = Coin
  fields = '__all__'
  
class CoinList(LoginRequiredMixin, ListView):
  model = Coin

class CoinDetail(LoginRequiredMixin, DetailView):
  model = Coin

class CoinUpdate(LoginRequiredMixin, UpdateView):
  model = Coin
  fields = ['name', 'mintage', 'image']

class CoinDelete(LoginRequiredMixin, DeleteView):
  model = Coin
  success_url = '/coins/'