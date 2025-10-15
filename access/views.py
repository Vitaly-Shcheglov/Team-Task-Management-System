from rest_framework import generics, permissions
from .models import AccessRolesRule, BusinessElement
from .serializers import AccessRolesRuleSerializer, BusinessElementSerializer

class AccessRolesRuleListCreateView(generics.ListCreateAPIView):
    queryset = AccessRolesRule.objects.all()
    serializerclass = AccessRolesRuleSerializer
    permissionclasses = (permissions.IsAdminUser,)

class AccessRolesRuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccessRolesRule.objects.all()
    serializerclass = AccessRolesRuleSerializer
    permissionclasses = (permissions.IsAdminUser,)

class BusinessElementListView(generics.ListAPIView):
    queryset = BusinessElement.objects.all()
    serializerclass = BusinessElementSerializer
    permissionclasses = (permissions.IsAuthenticated,)
