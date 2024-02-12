from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "image" ] # something like this
        
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profileimg"] # something like this


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        