from rest_framework import serializers
from customer.models import *
class GetcustomerSerializer(serializers.ModelSerializer):


    class Meta:
        model = Customers
        fields = "__all__"


class GetcustomerAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAddress
        fields = "__all__"


class GetcustomerDetailsAddressSerializer(serializers.ModelSerializer):

    customer_addresses = GetcustomerAddressSerializer(many=True)
    class Meta:
        model = Customers
        fields=('first_name','last_name','mobile_number','age','country','city','dob','customer_addresses')


