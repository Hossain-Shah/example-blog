import requests
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

class GetPostsList(APIView):
    def get(self, request, format=None):
        r = requests.get(f"https://jsonplaceholder.typicode.com/posts")
        return HttpResponse(r.json())

class GetPostDetails(APIView):
    def get(self, request, post_id, format=None):
        r = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        return HttpResponse(r.json())
    
class GetCommentsList(APIView):
    def get(self, request, post_id, format=None):
        r = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
        return HttpResponse(r.json())
