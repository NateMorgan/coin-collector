from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Collection(models.Model):
  name = models.CharField(max_length=30)
  description = models.TextField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('collections_detail', kwargs={'collection_id': self.id})

  def offers_current(self):
    print("Today's Date:")
    print(date.today())
    print("Latest Date:")
    print(self.offer_set.latest('date').date)
    print("Outcome")
    print((date.today() - self.offer_set.latest('date').date).days < 7)
    return (date.today() - self.offer_set.latest('date').date).days < 7

class Offer(models.Model):
  date = models.DateField()
  offerrer = models.CharField(max_length = 20)
  amount = models.IntegerField()
  collection = models.ForeignKey(Collection,on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.offerrer} offered {self.amount} on {self.date}"

  class Meta:
    ordering = ['-date']

class Coin(models.Model):
  name = models.CharField(max_length=50)
  mintage = models.IntegerField()
  image = models.CharField(max_length = 200)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('coins_detail', kwargs={'pk': self.id})