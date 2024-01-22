from rest_framework import serializers
from .models import Product
from django.db.models import Avg

class ProductSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source= 'owner.email')
    owner = serializers.ReadOnlyField(source= 'owner.id')
    
    
    class Meta:
        model = Product
        fields = '__all__'
        
        
        
    def to_representation(self, instance):
        reprezentation = super().to_representation(instance)
        reprezentation['ratings']= instance.rating.aggregate(
            Avg('rating')
        )
        
        reprezentation['rating_count']= instance.rating.count()
        return reprezentation
        
        
        