from django.shortcuts import render, redirect
# render를 통해 html 파일을 화면에 보여줌
from .models import Article

# Create your views here.
# 각각 html 파일로 연결해주는 함수 생성
def post(request):
    if request.method == "POST":
        new_post = Article()
        new_post.title = request.POST.get('title', '')
        new_post.content = request.POST.get('content', '')
        new_post.category_field = request.POST.get('category', '')
        new_post.save()
        return render(request, 'detail.html')
    elif request.method == "GET":
        all_tweet = Article.objects.all()
        return render(request, 'category.html', {"t"})



def list(request):
    if request.method == "GET":

