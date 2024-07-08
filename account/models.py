from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from account.managers import UserManager

class User(AbstractUser):
    CLIENT = 'individuals'
    SALESMAN = 'Legal_entities'
    ADMIN = 'admin'

    ROLE = (
        (CLIENT, 'физ-лица'),
        (SALESMAN, 'Юр-лица'),
        (ADMIN, 'Администратор')
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('-date_joined',)

    username = models.CharField(max_length=100,unique=True, verbose_name='фио')
    Idpassporta = models.CharField(max_length=7,verbose_name='ID possport')
    organ_vidachi = models.CharField(max_length=10, verbose_name='орган выдачи')
    personal_number_passport = models.CharField(max_length=14, verbose_name='персональный номер паспорта')
    avatar = ResizedImageField(size=[500, 500], crop=['middle', 'center'],
                               upload_to='avatars/', force_format='WEBP', quality=90, verbose_name='аватарка',
                               null=True, blank=True)
    phone = PhoneNumberField(max_length=100, unique=True, verbose_name='номер телефона')
    email = models.EmailField(null=True, verbose_name='электронная почта', unique=True)
    role = models.CharField('роль', choices=ROLE, default=CLIENT, max_length=15)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    @property
    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    get_full_name.fget.short_description = 'полное имя'

    def __str__(self):
        return f'{self.get_full_name or str(self.phone)}'

# Create your models here.

