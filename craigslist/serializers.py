from rest_framework import serializers

from .models import CraiglistInventory

from users.models import Staffs, Clients

class CraigListSerializer(serializers.ModelSerializer):

    client_name_company_name = serializers.SlugRelatedField(slug_field='full_name', 
                                queryset=Clients.objects.all())
    client_name_company_name = serializers.StringRelatedField()
    cl_admin_support = serializers.SlugRelatedField(slug_field='full_name', 
                                queryset=Staffs.objects.all())

    class Meta:
        model = CraiglistInventory
        fields = '__all__'
