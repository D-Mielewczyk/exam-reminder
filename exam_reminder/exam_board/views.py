from django.shortcuts import render
from .models import Exam
import datetime


def board(response):
    exams = Exam.objects.all().filter(date__gte=datetime.date.today()).order_by('date')
    return render(response, "exam_board/board.html", {'exams': exams})
