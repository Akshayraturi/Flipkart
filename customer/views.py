from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.models import*
from customer.serializers import*
# Create your views here.




class GetcustomerViews(APIView):
    def get(self,request):
        instance=Customers.objects.all()
        ser=GetcustomerSerializer(instance,many=True)
        return Response(ser.data)

    def post(self,request):
        params=request.data
        print("data--",params)
        ser=GetcustomerSerializer(data=params)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({"message":"Saved Successfully"})

class GetCustomersAddressViews(APIView):
    def get(self,request):
        instance=CustomerAddress.objects.all()
        ser=GetcustomerSerializer(instance,many=True)
        return Response(ser.data)

class GetCustomerDetailsAddressview(APIView):
    def get(self,request,pk):
        instances=Customers.objects.filter(id=pk)
        ser=GetcustomerDetailsAddressSerializer(instance,many=True)
        return Response(ser.data)