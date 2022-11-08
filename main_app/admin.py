from django.contrib import admin
# import your models here
from .models import Collection, Offer, Coin

# Register your models here
admin.site.register(Collection)
admin.site.register(Offer)
admin.site.register(Coin)