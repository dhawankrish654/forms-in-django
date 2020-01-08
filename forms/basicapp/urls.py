
from django.urls import path
from basicapp import views

urlpatterns = [
    path('',views.users,name='users'),
]
