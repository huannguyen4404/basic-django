from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

# def list(request):
#     Data = {'Posts': Post.objects.all().order_by("-date")}
#     return render(request, 'blog/blog.html', Data)
class PostListView(ListView):
    queryset = Post.objects.all().order_by('-date')
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 10

# def detail(request, id):
#     post = Post.objects.get(id=id)
#     return render(request, 'blog/detail.html', {'post': post})
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
