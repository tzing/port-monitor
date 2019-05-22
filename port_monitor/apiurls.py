from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('resolve/', views.resolve, name='resolve'),
    path('test/', views.check_connection, name='test'),
]
