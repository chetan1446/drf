from django.urls import path
from .views import show_student_list

urlpatterns = [
    path('show_student/',show_student_list),
    path('show_student/<int:id>/',show_student_list),
]
