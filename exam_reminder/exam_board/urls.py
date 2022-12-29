from django.urls import path
from . import views

urlpatterns = [
    path('', views.board, name="board"),
    path('<int:exam_id>', views.exam, name="exam"),
    path('past', views.past_board, name="past_board")
]