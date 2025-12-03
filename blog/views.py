from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')
def update(request, article_id):
	return HttpResponse("article_id: {}".format(article_id))
def hello(request):
    fortune=random.randit(1,3)
    isGreatFortune=False
    fortuneMessage=''
    if fortune == 1:
        fortuneMessage = 'Great Fortune'
        isGreatFortune = True  # 大吉の場合のみ True にする
    elif fortune == 2:
        fortuneMessage = 'Small Fortune'
        isGreatFortune = False
    else:
        fortuneMessage = 'Bad Fortune'
        isGreatFortune = False
    data={
         'name':'Alice',
         'weather':'CLOUDY',
         'wether_detail':['Temperature:23℃','Humidity:40%','Wind: 5m/s'],
         'isGreatFortune':isGreatFortune,
         'fortune':'Great Fortune!'
    }
    return render(request, 'blog/hello.html',data)