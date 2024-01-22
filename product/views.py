from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializer import ProductSerializer
from .permissions import IsAuthor
from rest_framework import permissions
from rest_framework.decorators import action
from rating.serializer import RatingSerializer
from rest_framework.response import Response
import logging
# Create your views here.


logger = logging.getLogger(__name__)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsAuthor(),)
        return (permissions.IsAuthenticatedOrReadOnly(),)
    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    
    
    @action(['GET','POST', 'DELETE'], detail=True)
    def rating(self, request, pk):
        product = self.get_object()
        user = request.user
        
        
        if request.method == 'GET':
            rating = product.rating.all()
            serializer = RatingSerializer(instance=rating, many=True)
            return Response(serializer.data, status=200)
        
        elif request.method =='POST':
            if product.rating.filter(owner = user).exists():
                return Response('Ты уже поставил райтинг на этот товар', status=400)
            
            serializer=RatingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(owner = user, product = product)
            return Response(serializer.data,status=201)
        
        
        else:
            if not product.rating.filter(owner=user).exists():
                return Response('Ты не можешь удалить потомучто ты не остовлял отзыв', status=400)
            
            rating = product.rating.get(owner=user)
            rating.delete()
            return Response('Успешно удалено', status=204)
        
            
                        
            
