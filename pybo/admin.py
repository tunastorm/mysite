from django.contrib import admin
from .models import Question

'''
1. django admin page document
    https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
'''

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)