from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('items/', views.item_index, name='item-index'),
    path('items/<int:item_id>/', views.item_detail, name='item-detail'),
    path('items/create/', views.ItemCreate.as_view(), name='item-create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='item-update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),
    path('items/<int:item_id>/add_market/', views.add_market, name='add_market'),
    path('markets/<int:pk>/update/', views.MarketUpdate.as_view(), name='market-update'),
    path('markets/<int:pk>/delete/', views.MarketDelete.as_view(), name='market-delete'),
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('tags/', views.TagList.as_view(), name='tags-index'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags-detail'),
    path('tags/create/', views.TagCreate.as_view(), name='tags-create'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tags-update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tags-delete'),
    path('items/<int:item_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc-tag'),
    path('items/<int:item_id>/unassoc_tag/<int:tag_id>/', views.unassoc_tag, name='unassoc-tag'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)