from django import forms
from .models import Exam


# class CreateExam(forms.ModelForm):
#     class Meta:
#         model = Exam
#         fields = ('name', 'subject', 'room', 'date', 'description')

class CreateExam(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

        widgets = {
            'date': forms.TextInput(attrs={'type': 'datetime-local'}),
        }
    # name = forms.CharField(max_length=200)
    # subject = forms.CharField(max_length=200)
    # room = forms.CharField(max_length=200)
    # date = forms.DateTimeField()
    # description = forms.CharField(max_length=2000, required=False)
    