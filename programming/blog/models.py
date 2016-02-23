from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Post(models.Model):   # 이 클래스는 모든 모델의 기본 클래스인 models.Model을 상속 받습니다.
    title = models.CharField(max_length=100, help_text='포스팅 제목을 100자 이내로 써주세요.')
    content = models.TextField()
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
