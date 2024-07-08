from django.contrib import admin
from .models import SmartContract, ContractParty, ContractSignature
admin.site.register(SmartContract),
admin.site.register(ContractParty)
admin.site.register(ContractSignature)
