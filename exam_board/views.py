from django.shortcuts import render, get_object_or_404, redirect
from .models import Exam
from .forms import CreateExam
from django.utils.timezone import now


def board(response):
    if response.method == "POST":
        form = CreateExam(response.POST)
        if form.is_valid():
            e = form.save()
            return redirect('exam', e.id)

    exams = Exam.objects.all().filter(date__gte=now()).order_by('date')
    f = CreateExam()
    return render(response, "exam_board/board.html", {'exams': exams, 'form': f})


def past_board(response):
    exams = Exam.objects.all().filter(date__lt=now()).order_by('-date')
    return render(response, "exam_board/board.html", {'exams': exams})


def exam(response, exam_id):
    e = get_object_or_404(Exam, id=exam_id)
    if response.method == "POST":
        form = CreateExam(response.POST, instance=e)
        if form.is_valid():
            form.save()

    f = CreateExam(initial=e.__dict__)
    return render(response, 'exam_board/exam.html', {'exam': e, 'form': f})
