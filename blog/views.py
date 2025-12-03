from django.shortcuts import render
import random
fortune=random.randint(1,3)
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')
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