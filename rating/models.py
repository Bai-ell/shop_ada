from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
# Create your models here.


User = get_user_model()

class Rating(models.Model):
    RATING_CHICES = (
        (1,'too bad'),
        (2,'bad'),
        (3,'normal'),
        (4,'good'),
        (5,'excellent'),
    )
    
    
    product = models.ForeignKey(Product, related_name = 'rating', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name = 'raitings', on_delete = models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices = RATING_CHICES)
    created_at = models.DateTimeField(auto_now_add = True)
    
    
    class Meta:
        unique_together = ['owner', 'product']
        
     
     
     
    