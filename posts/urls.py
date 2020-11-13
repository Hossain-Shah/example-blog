from django.urls import path
from posts.views import GetPostsList, GetPostDetails, GetCommentsList

urlpatterns = [
    path('', GetPostsList.as_view()),
    path('<int:post_id>', GetPostDetails.as_view()),
    path('<int:post_id>/comments', GetCommentsList.as_view())
]
