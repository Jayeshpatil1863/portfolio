from django.contrib import admin
from django.urls import path
from first import views as v

app_name = 'first'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home,name='home'),
    path('survay/', v.survay, name='survay'),
]
