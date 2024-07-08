from django.urls import path,include
from .views import (
    SmartContractListCreateView, SmartContractRetrieveUpdateDestroyView,
    ContractSignatureListCreateView, ContractSignatureRetrieveUpdateDestroyView,
    ContractPartyListCreateView, ContractPartyRetrieveUpdateDestroyView
)

urlpatterns = [
    path('contracts/', SmartContractListCreateView.as_view(), name='contract-list-create'),
    path('contracts/<int:pk>/', SmartContractRetrieveUpdateDestroyView.as_view(), name='contract-detail'),
    path('signatures/', ContractSignatureListCreateView.as_view(), name='signature-list-create'),
    path('signatures/<int:pk>/', ContractSignatureRetrieveUpdateDestroyView.as_view(), name='signature-detail'),
    path('parties/', ContractPartyListCreateView.as_view(), name='party-list-create'),
    path('parties/<int:pk>/', ContractPartyRetrieveUpdateDestroyView.as_view(), name='party-detail'),
    path('auth/', include('core.api.auth.urls')),
]
