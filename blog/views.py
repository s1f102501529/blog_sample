from django.shortcuts import render,redirect
import random
fortune=random.randint(1,3)
# Create your views here.
from django.http import HttpResponse
from django.utils import timezone

from blog.models import Article, Comment
from django.http import Http404
def index(request):
    if request.method == 'POST':
         article = Article(title=request.POST['title'], body=request.POST['text'])
         article.save()
         return redirect(detail,article.id)
    if ('sort' in request.GET):
         if request.GET['sort'] == 'like':
              articles=Article.objects.order_by('-like')
         else:
              articles = Article.objects.order_by('-posted_at')
    else:
         articles=Article.objects.order_by('-posted_at')
    context = {
        "articles": articles
    }
    return render(request, 'blog/index.html', context)
def update(request, article_id):
	return HttpResponse("article_id: {}".format(article_id))
def hello(request):
    fortune
    isGreatFortune=False
    fortuneMessage=''
    data={
         'name':'Alice',
         'weather':'CLOUDY',
         'wether_detail':['Temperature:23℃','Humidity:40%','Wind: 5m/s'],
         'isGreatFortune': isGreatFortune,
         'fortune': fortuneMessage
    }
    return render(request, 'blog/hello.html',data)
def redirect_test(request):
     return redirect(hello)
def detail(request,article_id):
     try:
          article = Article.objects.get(pk=article_id)
     except Article.DoesNotExist:
          raise Http404("Article dose not exist")
     
     if request.method == 'POST':
          comment = Comment(article=article, text=request.POST['text'])
          comment.save()
     
     context={
          "article":article,
          'comments':article.comments.order_by('-posted_at')
     }
     return render(request,"blog/detail.html",context)
def update(request,article_id):
     try:
          article = Article.objects.get(pk=article_id)
     except Article.DoesNotExist:
          raise Http404("Article dose not exist")
     context={
          "article_id": article_id
     }
     return render(request,"blog/edit.html",context)
def delete(request, article_id):
     try:
          article = Article.objects.get(pk=article_id)
     except Article.DoesNotExist:
          raise Http404("Article dose not exist")
     article.delete()

     return redirect(index)
def like(request, article_id):
     try:
          article = Article.objects.get(pk=article_id)
          article.like += 1
          article.save()
     except Article.DoesNotExist:
          raise Http404("Article dose not exist")
     

     return redirect(detail,article_id)
