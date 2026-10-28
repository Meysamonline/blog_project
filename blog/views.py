from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView
from numpy import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import NewPostForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import auth

from .models import Post

# def post_list_view(request):
#     posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html', {'posts_list': posts_list})
class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
        return posts_list

# 
# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     post = None
#     #     print("excepted")
#     return render(request, 'blog/post_detail.html', {'post': post})
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    contex_detail_view = 'post'

# def post_create_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = NewPostForm()
#     return render(request, 'blog/create_post.html', context={'form': form})

class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/create_post.html'

# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#     return render(request, 'blog/create_post.html', context={'form': form})

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/create_post.html'




class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')