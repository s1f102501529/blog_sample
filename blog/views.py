from django.shortcuts import render,redirect
import random
fortune=random.randint(1,3)
# Create your views here.
from django.http import HttpResponse
from django.utils import timezone

def index(request):
    context = {
        "articles": [
            {
                "id": 1,
                "title": "Post 01",
                "body": "test post.\nLorem ipsum dolor sit amet, \nconsectetur adipiscing elit,\n sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n", 
                "posted_at": timezone.now # option
            }
        ]
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
     context={
          "article_id":article_id
     }
     return render(request,"blog/tbd.html",context)
def update(request,article_id):
     context={
          "article_id": article_id
     }
     return render(request,"blog/tbd.html",context)
def delete(request, article_id):
     return redirect(index)