from django.urls import path

from .apis.views import CreateUserView, CreateTokenView, ManageUserView


app_name = "users"

urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create"),
    path("me/", ManageUserView.as_view(), name="me"),
    path("token", CreateTokenView.as_view(), name="token"),
]
