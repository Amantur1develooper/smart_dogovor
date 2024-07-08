from rest_framework import serializers
from ..models import SmartContract, ContractSignature, ContractParty

class ContractSignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractSignature
        fields = ['id', 'contract', 'signer', 'signed_at']

class ContractPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractParty
        fields = ['id', 'contract', 'party_name', 'party_email']

class SmartContractSerializer(serializers.ModelSerializer):
    signatures = ContractSignatureSerializer(many=True, read_only=True)
    parties = ContractPartySerializer(many=True, read_only=True)

    class Meta:
        model = SmartContract
        fields = ['id', 'creator', 'title', 'content', 'status', 'created_at', 'updated_at', 
                  'description', 'podpis1', 'podpis2', 'previous_hash', 'hash', 'signatures', 'parties']
        read_only_fields = ['id', 'created_at', 'updated_at', 'hash']
