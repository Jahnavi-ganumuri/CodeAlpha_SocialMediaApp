from django.urls import path

from .views import (
    RegisterView,
    SearchUsers,
    ProfileView,
    FollowUser
)


urlpatterns = [

    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),


    path(
        "search/",
        SearchUsers.as_view(),
        name="search-users"
    ),


    path(
        "profile/<int:pk>/",
        ProfileView.as_view(),
        name="profile"
    ),


    path(
        "follow/<int:id>/",
        FollowUser.as_view(),
        name="follow-user"
    ),

]