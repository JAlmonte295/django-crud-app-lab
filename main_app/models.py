from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


MARKET = (
    ('A', 'Amazon'),
    ('E', 'eBay'),
    ('F', 'Facebook Marketplace'),
    ('O', 'OfferUp'),
    ('P', 'Private Buyer'),
)

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    image = models.ImageField(upload_to='items/', blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'item_id': self.id})
    
class Market(models.Model):
    outlet = models.CharField(max_length=1, choices=MARKET, default=MARKET[0][0])
    price = models.DecimalField('Current Selling Price',max_digits=10, decimal_places=2)

    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_outlet_display()} price: {self.price}"
    
    class Meta:
        ordering = ['-price']

class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tags-detail', kwargs={'pk': self.id})