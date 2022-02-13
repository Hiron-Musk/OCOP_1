from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    has_answer = models.BooleanField(default=True)  # 답변가능 여부

    class Meta:
        db_table = 'pybo_category'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pybo:pybo', args=[self.name])

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, blank=True, related_name='voter_question')  # 추천인 추가
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_question')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.subject # id 값 대신 제목 표시

    def get_absolute_url(self):
        return reverse('pybo:question_detail', args=[self.id])

    def get_recent_comments(self):
        return self.comment_set.all().order_by('-create_date')[:5]

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='category_answer')  # 추천인 추가
