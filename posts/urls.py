from django.urls import path
from posts.views import GetPostsList, GetPostDetails

urlpatterns = [
    path('', GetPostsList.as_view()),
    path('<int:id>', GetPostDetails.as_view())
]
