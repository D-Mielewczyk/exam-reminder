from django import forms


class CreateExam(forms.Form):
    name = forms.CharField(max_length=200)
    subject = forms.CharField(max_length=200)
    room = forms.CharField(max_length=200)
    date = forms.DateTimeField()
    description = forms.CharField(max_length=2000, blank=True)
    