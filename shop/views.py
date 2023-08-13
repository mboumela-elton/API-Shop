from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Category, Product
from shop.serializers import CategorySerializer, ProductSerializer

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from shop.models import Category
from shop.serializers import CategorySerializer

class CategoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

class ProductAPIView(APIView):

    def get(self, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)