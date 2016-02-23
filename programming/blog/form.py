from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    is_agree = form.BooleanField(label='약관동의',
            error_messages={'required: '약관에 동의해 주셔야 서비스 이용이 가능합니다."})

    class Meta:
        model = Post
        fields = '__all__'

