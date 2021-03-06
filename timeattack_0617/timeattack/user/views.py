from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import login, authenticate, logout
from .models import User
from django.contrib.auth.hashers import make_password



class UserView(APIView): # CBV 방식
    
    def get(self, request):
        return Response({'message': 'get method!!'})
        
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        password = make_password(password, salt=None, hasher='default')
        new_user = User.objects.create(username=username, password=password)
        new_user.save()
        return Response({'message': 'post method!!'})



class UserApiView(APIView):
    permission_classes = [permissions.AllowAny]
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')


        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})

        login(request, user)
        return Response({"message": "로그인 성공!!"})
    
    # 삭제
    def delete(self, request):
        logout(request)
        return Response({"message":"로그아웃 성공!!!"})