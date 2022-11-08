from django.db import models
from django.urls import reverse

# Create your models here.
class Collection(models.Model):
  name = models.CharField(max_length=30)
  description = models.TextField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('collections_detail', kwargs={'collection_id': self.id})