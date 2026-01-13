from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('items/', views.item_index, name='item-index'),
    path('items/<int:item_id>/', views.item_detail, name='item-detail'),
    path('items/create/', views.ItemCreate.as_view(), name='item-create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='item-update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),
    path('items/<int:item_id>/add_market/', views.add_market, name='add_market'),
    path('markets/<int:pk>/update/', views.MarketUpdate.as_view(), name='market-update'),
    path('markets/<int:pk>/delete/', views.MarketDelete.as_view(), name='market-delete'),
]