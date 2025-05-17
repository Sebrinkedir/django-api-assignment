from django import forms
from .models import Post, Profile

# Form for creating or updating posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Fields for the post (title and content)

# Form for updating the profile (bio and profile picture)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
  # Fields to update in the profile

