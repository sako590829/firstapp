from .models import Post
from django import forms 


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('text', 'img')
    
    def clean(self):
        cleaned_data = super().clean()
        img = cleaned_data.get('img')
        if not img:
            cleaned_data['img'] = None
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['img'].required = False  # 画像フィールドを必須でないようにする





