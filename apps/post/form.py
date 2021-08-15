from django.forms import ModelForm, fields
from apps.post.models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields=('titulo','descripcion','imagen')