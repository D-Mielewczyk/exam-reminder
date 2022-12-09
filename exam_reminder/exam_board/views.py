from django.shortcuts import render


# Create your views here.
def board(response):
    return render(response, "exam_board/base.html", {})
