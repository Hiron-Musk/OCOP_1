from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.pybo, name='pybo'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('question/create/', views.question_create, name = 'question_create'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),

    #수정
    path('question/modify/<int:question_id>', views.question_modify, name='question_modify'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),

    #삭제
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),

    # 추천
    path('vote/question/<int:question_id>/', views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', views.vote_answer, name='vote_answer'),

    #category
    path('question/list/', views.pybo, name='pybo'),
    path('question/list/<str:category_name>/', views.pybo, name='pybo'),
    path('question/detail/<int:question_id>/', views.detail, name='detail'),
    path('question/create/<str:category_name>/', views.question_create, name='question_create'),
]
