
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .models import Article, Writer, ArticleWriter
from django.urls import reverse

from django.http import HttpResponse
from .models import Article, Comment
from .forms import CommentForm

def home(request):
    return render(request, "webApp/home.html")

def article(request):
    list_of_articles = Article.objects.all()

    for article in list_of_articles:
        article.article_writers_list = article.article_writers.all()

    # Pass both articles and their writers to the template
    context = {
        "articles": list_of_articles,
    }

    return render(request, "webApp/article.html", context)

def articleDetail(request, article_slug):
    article = Article.objects.get(slug=article_slug)
    article_writers = article.article_writers.all()
    print(article_writers.all())
    comments = article.comments.all()
    print(comments)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user  # assuming you have user info
            new_comment.save()
            return redirect(reverse('article_detail', kwargs={'article_slug': article.slug}))
    else:
        comment_form = CommentForm()

    context = {
        "article": article,
        "article_writers": article_writers,
        'comment_form': comment_form,
        'comments': comments,
    }

    return render(request, "webApp/article-detail.html", context)


def writerDetail(request, writer_id):
    writer = get_object_or_404(Writer, pk=writer_id)
    print(writer,'object')
    # articles = writer.written_articles.all()
    articles = Article.objects.filter(article_writers__writer=writer)
    print(writer,'object',articles)
    return render(request, "webApp/writer-detail.html", {"writer": writer, "articles": articles})

def writer(request):
    list_of_writer = Writer.objects.all()
    for writer in list_of_writer:
        print(writer.pk)
    return render(request, "webApp/writer.html", {"writers": list_of_writer})

def aboutus(request):
    return render(request, "webApp/aboutus.html")



from haystack.query import SearchQuerySet
from django.shortcuts import render

def search(request):
    query = request.GET.get('q')
    results = SearchQuerySet().filter(content__icontains=query) 
    return render(request, 'search/results.html', {'results': results})


def deleteComment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    article_slug = comment.article.slug
    comment.delete()
    print("Comment deleted")
    return redirect(reverse('article_detail', kwargs={'article_slug': article_slug}))
