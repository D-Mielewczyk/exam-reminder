from django.urls import path
from . import views

urlpatterns = [
    path('', views.board, name="board"),
    path('<int:exam_id>', views.exam, name="exam")
]