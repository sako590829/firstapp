from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 2
    ordering = ['-serial_number'] 

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()

            if not form.cleaned_data['img']:
                post.img = None
            else:
                post.img = form.cleaned_data['img']

            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()

            if not form.cleaned_data['img']:
                post.img = None
            else:
                post.img = form.cleaned_data['img']

            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
