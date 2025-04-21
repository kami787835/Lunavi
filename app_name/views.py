from rest_framework import generics
from rest_framework.generics import ListAPIView
from .models import Product, Order
from .serializers import ProductSerializer, ProductListSerializer, OrderSerializer
from django.http import JsonResponse

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class =ProductSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class YourAPIView(APIView):
    """
    Your API View Description
    """

    def get(self, request):
        """
        GET request description
        """
        # Your code here
        return Response(data={}, status=status.HTTP_200_OK)

def product_list(request):
    products = Product.objects.all()
    data = {'products': list(products.values())}
    return JsonResponse(data)

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer