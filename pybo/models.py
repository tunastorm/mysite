from django.db import models
from django.contrib.auth.models import User

'''
1. 각 field 설명 document
    https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types

2. query 만들기 document 
    https://docs.djangoproject.com/en/3.0/topics/db/queries/

'''

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200) # 글자 수가 제한된 텍스트
    content = models.TextField() # 글자 수를 제한할 수 없는 텍스트
    create_date = models.DateTimeField() 
    modify_date = models.DateTimeField(null=True, blank=True) #blank=True form.is_valid()로 입력데이터 검사시 값이 없어도 된다는 뜻
    voter = models.ManyToManyField(User, related_name='voter_question')
    
    def __str__(self): 
        return self.subject
    '''
    1. 모델에 메서드가 추가될 때는 makemigration 과 migrate를 수행할 필요 없다
    # 주석
        1) makemigration
           - magrate 명령어 실행시 수행할 작업을 생성한다
           - <app_name>/_pycache_/000<n>_initial.py
           - sqlmigrate 명령어로 각 작업파일별로 어떤 Query가 실행되는지 출력할 수 있다
        2) migrate
           - model의 변경사항을 DB에 반영한다
    '''
    
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # null=True 널 값 허용
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    '''
    1. Question 모델을 Foreign Key로 사용
    2. -> models.CASCADE 연결된 Question이 삭제될 때 해당되는 답변도 함께 삭제  
    '''
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

