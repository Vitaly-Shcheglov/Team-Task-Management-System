from django.urls import path
from .views import (AccessRolesRuleListCreateView, AccessRolesRuleDetailView,
                    BusinessElementListView)

urlpatterns = [
    path('rules/', AccessRolesRuleListCreateView.as_view(), name='access-rules-list'),
    path('rules/<int:pk>/', AccessRolesRuleDetailView.as_view(), name='access-rule-detail'),
    path('elements/', BusinessElementListView.as_view(), name='business-elements-list'),
]
