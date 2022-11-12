from django.urls import path, include 
from . import views
from django.contrib.auth import urls

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('about/', views.about, name='about'),
  path('collections/', views.collections_index, name='collections_index'),
  path('collections/<int:collection_id>/', views.collections_detail, name='collections_detail'),
  path('collections/create/', views.CollectionCreate.as_view(), name='collections_create'),
  path('collections/<int:pk>/update/', views.CollectionUpdate.as_view(), name='collections_update'),
  path('collections/<int:pk>/delete/', views.CollectionDelete.as_view(), name='collections_delete'),
  path('collections/<int:collection_id>/add_offer/', views.add_offer, name='add_offer'),
  path('collections/<int:collection_id>/assoc_coin/<int:coin_id>/', views.assoc_coin, name='assoc_coin'),
  path('coins/create/', views.CoinCreate.as_view(), name='coins_create'),
  path('coins/', views.CoinList.as_view(), name='coins_index'),
  path('coins/<int:pk>/', views.CoinDetail.as_view(), name='coins_detail'),
  path('coins/<int:pk>/update/', views.CoinUpdate.as_view(), name='coins_update'),
  path('coins/<int:pk>/delete', views.CoinDelete.as_view(), name='coins_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]