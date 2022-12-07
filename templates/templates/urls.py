from django.urls import path
from temp_app import views

urlpatterns = [
    path('', views.form)
]
