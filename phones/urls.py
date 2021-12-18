from django.urls import path
from phones.views import getInfo
app_name = 'phones'
urlpatterns=[
    path('get_phones/',getInfo,name='info')
]