from django.urls import path

from .views import PostView, CommentView, like_post


urlpatterns = [

    path(
        "posts/",
        PostView.as_view({
            "get": "list",
            "post": "create"
        }),
        name="posts"
    ),


    path(
        "posts/<int:id>/",
        PostView.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }),
        name="post-detail"
    ),


    path(
        "posts/<int:id>/like/",
        like_post,
        name="like-post"
    ),


    path(
        "comments/",
        CommentView.as_view({
            "get": "list",
            "post": "create"
        }),
        name="comments"
    ),


    path(
        "comments/<int:pk>/",
        CommentView.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }),
        name="comment-detail"
    ),

]