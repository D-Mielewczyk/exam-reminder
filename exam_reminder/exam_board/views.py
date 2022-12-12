from django.shortcuts import render, get_object_or_404
from .models import Exam
import datetime


def board(response):
    exams = Exam.objects.all().filter(date__gte=datetime.date.today()).order_by('date')
    return render(response, "exam_board/board.html", {'exams': exams})

def exam(response, exam_id):
    e = get_object_or_404(Exam, id=exam_id)
    return render(response, 'exam_board/exam.html', {'exam': e})