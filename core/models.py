from django.db import models
from django.contrib.auth import get_user_model
import hashlib
from django.contrib.auth.models import User
from django.db import models

User = get_user_model()


class SmartContract(models.Model):
    STATUS_CHOICES = [
        ('черновик', 'Черновик'),
        ('ожидается подпись', 'Ожидается подпись'),
        ('подписано', 'Подписано'),
        ('хэшированный', 'Хэшированный'),
    ]

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_contracts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description =models.CharField(max_length=1000,blank=True, null=True)
    podpis1 = models.FileField(upload_to='podpisi1', blank=True,null=True)
    podpis2 = models.FileField(upload_to='podpisi2', blank=True,null=True)
    previous_hash = models.CharField(max_length=64,null=True, blank=True)
    hash = models.CharField(max_length=64, blank=True,null=True)
    

    def save(self, *args, **kwargs):
        if self.status == 'подписано':
            self.status == 'хэшированный'
            self.hash = self.compute_hash()
        super(SmartContract, self).save(*args, **kwargs)
        
    def __str__(self):
        return "контракт{}".format(self.id)
    
    def compute_hash(self):
        signatures = self.signatures.all()
        signatures_str = ''.join([str(signature) for signature in signatures])

        # Получаем все стороны контракта
        parties = self.parties.all()
        parties_str = ''.join([str(party) for party in parties])

        # Формируем строку для хэширования
        block_string = "{}{}{}{}{}{}{}{}{}{}{}{}{}".format(
            self.id, self.creator, self.title, self.content, self.status, self.created_at,
            self.updated_at, self.description, self.podpis1, self.podpis2, signatures_str,
            parties_str, self.previous_hash
        )
        return hashlib.sha256(block_string.encode()).hexdigest()


class ContractSignature(models.Model):
    contract = models.ForeignKey(SmartContract, on_delete=models.CASCADE, related_name='signatures')
    signer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='signed_contracts')
    signed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.signer.username} signed {self.contract.title}'


class ContractParty(models.Model):
    contract = models.ForeignKey(SmartContract, on_delete=models.CASCADE, related_name='parties')
    party_name = models.CharField(max_length=255)
    party_email = models.EmailField()

    def __str__(self):
        return f'{self.party_name} ({self.party_email})'

