from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post


def gallery_first(request):
    return render(request, 'blog/post/gallery1.html')

def gallery_second(request):
    return render(request, 'blog/post/gallery2.html')

def gallery_third(request):
    return render(request, 'blog/post/gallery3.html')

def farakhan(request):
    return render(request, 'blog/post/farakhan.html')

def about(request):
    return render(request, 'blog/post/about.html')

def olom_payeh(request):
    return render(request, 'blog/post/olom_payeh.html')

def olom_ensani(request):
    return render(request, 'blog/post/olom_ensani.html')

def fani(request):
    return render(request, 'blog/post/fani.html')

def pezeshki(request):
    return render(request, 'blog/post/pezeshki.html')

def keshavarzi(request):
    return render(request, 'blog/post/keshavarzi.html')

def dampezeshki(request):
    return render(request, 'blog/post/dampezeshki.html')

def honar(request):
    return render(request, 'blog/post/honar.html')

def introduction(request):
    return render(request, 'blog/post/introduction.html')

def executive(request):
    return render(request, 'blog/post/executive.html')

def purpose(request):
    return render(request, 'blog/post/purpose.html')

def foundation(request):
    return render(request, 'blog/post/foundation.html')

def news(request):
    return render(request, 'blog/post/news.html')

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/news.html',
                  {'post': post})

class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'