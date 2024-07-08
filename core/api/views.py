from rest_framework import generics
from ..models import SmartContract, ContractSignature, ContractParty
from .serializers import SmartContractSerializer, ContractSignatureSerializer, ContractPartySerializer

class SmartContractListCreateView(generics.ListCreateAPIView):
    queryset = SmartContract.objects.all()
    serializer_class = SmartContractSerializer

class SmartContractRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SmartContract.objects.all()
    serializer_class = SmartContractSerializer

class ContractSignatureListCreateView(generics.ListCreateAPIView):
    queryset = ContractSignature.objects.all()
    serializer_class = ContractSignatureSerializer

class ContractSignatureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContractSignature.objects.all()
    serializer_class = ContractSignatureSerializer

class ContractPartyListCreateView(generics.ListCreateAPIView):
    queryset = ContractParty.objects.all()
    serializer_class = ContractPartySerializer

class ContractPartyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContractParty.objects.all()
    serializer_class = ContractPartySerializer
