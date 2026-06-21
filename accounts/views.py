from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema

from django.contrib.auth.models import User

from .serializers import RegisterSerializer, ProfileSerializer
from .models import Profile, Follow
from drf_spectacular.utils import extend_schema, OpenApiParameter

# Register new user
class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer



# Search users



class SearchUsers(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="q",
                description="Search username",
                required=True,
                type=str
            )
        ]
    )
    def get(self, request):

        q = request.GET.get("q")

        users = User.objects.filter(
            username__icontains=q
        )

        return Response(
            [
                {
                    "username": user.username
                }
                for user in users
            ]
        )

# Profile view
class ProfileView(generics.RetrieveUpdateAPIView):

    queryset = Profile.objects.all()

    serializer_class = ProfileSerializer



# Follow / Unfollow user
class FollowUser(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
    request=None,
    responses={200: dict}
)
    def post(self, request, id):

        current_user = request.user

        try:
            user_to_follow = User.objects.get(id=id)

        except User.DoesNotExist:

            return Response(
                {
                    "message": "User not found"
                },
                status=404
            )


        if current_user == user_to_follow:

            return Response(
                {
                    "message": "You cannot follow yourself"
                }
            )


        existing_follow = Follow.objects.filter(
            follower=current_user,
            following=user_to_follow
        )


        if existing_follow.exists():

            existing_follow.delete()

            return Response(
                {
                    "message": "Unfollowed user"
                }
            )


        Follow.objects.create(
            follower=current_user,
            following=user_to_follow
        )


        return Response(
            {
                "message": "User followed"
            }
        )