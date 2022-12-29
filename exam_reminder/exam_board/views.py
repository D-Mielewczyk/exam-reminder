from django.shortcuts import render, get_object_or_404
from .models import Exam
from .forms import CreateExam
from django.utils.timezone import now


def board(response):
    exams = Exam.objects.all().filter(date__gte=now()).order_by('date')
    return render(response, "exam_board/board.html", {'exams': exams})


def past_board(response):
    exams = Exam.objects.all().filter(date__lt=now()).order_by('-date')
    return render(response, "exam_board/board.html", {'exams': exams})


def exam(response, exam_id):
    e = get_object_or_404(Exam, id=exam_id)
    f = CreateExam()
    return render(response, 'exam_board/exam.html', {'exam': e, 'form': f})
