from django.urls import path

from .apis import views

app_name = "tinyurl"

urlpatterns = [
    path("original/", views.UrlDetailView.as_view(), name="original_api"),
    path("tinyurl/", views.UrlCreateView.as_view(), name="tinyurl_api"),
]
