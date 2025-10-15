from rest_framework import serializers
from .models import BusinessElement, AccessRolesRule

class BusinessElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessElement
        fields = ('id', 'name', 'description')

class AccessRolesRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessRolesRule
        fields = (
            'id', 'role', 'businesselement',
            'readpermission', 'readallpermission',
            'createpermission', 'updatepermission', 'updateallpermission',
            'deletepermission', 'deleteallpermission'
        )
