from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('get_date/', index, name='get_date'),
]
