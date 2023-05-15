from django.shortcuts import render
from product.models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.
@api_view(["GET", "POST"])
def product_home_page(request):
    if request.method == "GET":
        all_product = Product.objects.all()
        serializer = ProductSerializer(all_product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Nice work!!",
                            "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response("Invalid data entered")
    
@api_view(["GET", "PUT", "DELETE"])
def product_detail_page(request, pk):
    if request.method == "GET":
        single_product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(single_product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == "PUT":
        single_product = Product.objects.get(id=id)
        serializer = ProductSerializer(single_product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        single_product = Product.Object.get(id=id)
        single_product.delete()
        return Response("Product has been deleted", status=status.HTTP_204_NO_CONTENT)