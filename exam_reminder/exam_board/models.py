from django.db import models
from django import forms


class Exam(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    room = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.name


class ExamFrom(forms.Form):
    class Meta:
        model = Exam
        fields = ('name', 'subject', 'room', 'date', 'description')

    def __init__(self, *args, **kwargs):
        super(ExamFrom, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
