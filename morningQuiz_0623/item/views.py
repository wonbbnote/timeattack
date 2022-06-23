from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from item.models import Item

from item.serializer import ItemSerializer

# Create your views here.

class ItemView(APIView):
    def get(self, request):
        products = Item.objects.all()
        return Response(ItemSerializer(products, many=True).data)

    def post(self, request):
        product_serializer = ItemSerializer(data=request.data)
        print(product_serializer)
        return Response({"mds":"post method!"})