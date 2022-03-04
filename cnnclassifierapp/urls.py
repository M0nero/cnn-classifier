from django.urls import path

from . import views

app_name = 'cnnclassifierapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('submit/', views.get_output, name='submit')
]