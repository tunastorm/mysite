from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question

import logging

logger = logging.getLogger('pybo')

def index(request):
    logger.info('INFO 레벨로 출력')
    '''
    pybo 목록 출력
    
    1. render 함수
        : 파이썬 데이터를 템플릿에 적용하여 HTML로 변환하는 함수
        
        1) template
            : Django에서 사용하는 tag를 사용할 수 있는 HTML 파일
    '''
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    so = request.GET.get('so', 'recent') # 정렬기준
    
    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', 'create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        question_list = Question.objects.order_by('-create_date')
        
    
    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # 제목검색
            Q(content__icontains=kw) | # 내용검색
            Q(author__username__icontains=kw) | # 질문 작성자 검색
            Q(answer__author__username__icontains=kw) # 답변 작성자 검색
        ).distinct()
    
    # 페이징 처리 
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page) 
    
    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    '''
    pybo 내용 출력
    '''
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)