from django import forms
from pybo.models import Question, Answer

'''
1. Django form document
    https://docs.djangoproject.com/en/3.0/topics/forms/
'''


class QuestionForm(forms.ModelForm):
    '''
    Question 모델과 연결된 Form
    '''
    class Meta: # innerclass, 반드시 필요
        model = Question
        fields = ['subject', 'content']
        # {{forms.as_p}} 사용해 HTML 자동생성시 bootstrap 적용 방법
        '''widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }'''
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
        