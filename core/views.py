from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages  
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Post, Profile
from .forms import PostForm, ProfileUpdateForm  # Import ProfileUpdateForm
from rest_framework.viewsets import ModelViewSet  
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

# List View
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'core/post_list.html', {'posts': posts})

# Detail View
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'core/post_detail.html', {'post': post})

# Create View
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'core/post_form.html', {'form': form})

# Update View
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'core/post_form.html', {'form': form})

# Delete View with permission check
def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'core/post_confirm_delete.html', {'post': post})

# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Profile created automatically by signal
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

# Profile View
@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'core/profile.html', {'profile': profile})

# Profile Update View
@login_required
def profile_update(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'core/profile_update.html', {'form': form})
# REST API ViewSet for Post model
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]