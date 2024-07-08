# Generated by Django 5.0.6 on 2024-07-08 09:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('черновик', 'Черновик'), ('ожидается подпись', 'Ожидается подпись'), ('подписано', 'Подписано'), ('хэшированный', 'Хэшированный')], default='draft', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('podpis1', models.FileField(blank=True, null=True, upload_to='podpisi1')),
                ('podpis2', models.FileField(blank=True, null=True, upload_to='podpisi2')),
                ('previous_hash', models.CharField(blank=True, max_length=64, null=True)),
                ('hash', models.CharField(blank=True, max_length=64, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_contracts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContractSignature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signed_at', models.DateTimeField(auto_now_add=True)),
                ('signer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signed_contracts', to=settings.AUTH_USER_MODEL)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signatures', to='core.smartcontract')),
            ],
        ),
        migrations.CreateModel(
            name='ContractParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=255)),
                ('party_email', models.EmailField(max_length=254)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parties', to='core.smartcontract')),
            ],
        ),
    ]