from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_api_view),
    path('register/', views.register_api_view),
]