from django.shortcuts import render
from django.http import HttpResponse

class Collection:
  def __init__(self, name, description):
    self.name = name
    self.description = description

collections = [
  Collection('Buffalo Nickles',"Bag O' Buffalo Nickles"),
  Collection('Morgan Silver Dollars',"Prize Possesstion of my Family"),
  Collection('Big Fricken Coins',"Not only are they big, they are also heavy!")

]




def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def collections_index(request):
  return render(request, 'collections/index.html', {'collections': collections})