from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, OpenApiResponse

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer



class PostView(ModelViewSet):

    queryset = Post.objects.all()

    serializer_class = PostSerializer



class CommentView(ModelViewSet):

    queryset = Comment.objects.all()

    serializer_class = CommentSerializer



@extend_schema(
    request=None,
    responses={
        200: OpenApiResponse(
            description="Like or unlike post response"
        )
    }
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like_post(request, id):

    try:
        post = Post.objects.get(id=id)

    except Post.DoesNotExist:

        return Response(
            {
                "message": "Post not found"
            },
            status=404
        )


    user = request.user


    if user in post.likes.all():

        post.likes.remove(user)

        return Response(
            {
                "message": "Post unliked"
            }
        )


    post.likes.add(user)

    return Response(
        {
            "message": "Post liked"
        }
    )