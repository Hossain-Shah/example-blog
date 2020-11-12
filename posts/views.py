import requests
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

class GetPostsList(APIView):
    def get(self, request, format=None):
        r = requests.get("https://jsonplaceholder.typicode.com/posts")
        return HttpResponse(r.json())

class GetPostDetails(APIView):
    def get(self, request, id, format=None):
        r = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
        return HttpResponse(r.json())
