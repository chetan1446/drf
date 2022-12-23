from django.urls import path
from .views import show_patients

urlpatterns = [
    path('show_patient/',show_patients),
    path('show_patient/<int:id>/',show_patients)
]