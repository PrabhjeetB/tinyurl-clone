from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from users.models import User
from .serializers import TinyUrlSerializer, OriginalUrlSerializer
from tinyurl.utils.tiny import get_original_url, get_tinyurl


class UrlCreateView(CreateAPIView):
    serializer_class = OriginalUrlSerializer

    def post(self, request, *args, **kwargs):
        api_dev_key = request.data.get("api_dev_key", None)
        if api_dev_key:
            user = User.objects.get(api_dev_key=api_dev_key)
            if not user:
                return Response(
                    {"error": "Invalid api_dev_key"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response({"error": "Missing api_dev_key"})
        original_url = request.data.get("original_url", None)
        if original_url:
            short_url = get_tinyurl(original_url)
            return Response(
                {"original_url": original_url, "short_url": short_url},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"original_url": original_url, "error": "Missing short_url"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UrlDetailView(GenericAPIView):
    serializer_class = TinyUrlSerializer

    def post(self, request, *args, **kwargs):
        api_dev_key = request.data.get("api_dev_key", None)
        if api_dev_key:
            user = User.objects.get(api_dev_key=api_dev_key)
            if not user:
                return Response(
                    {"error": "Invalid api_dev_key"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response({"error": "Missing api_dev_key"})
        short_url = request.data.get("short_url")
        original_url = get_original_url(short_url)
        if original_url:
            return Response(
                {"original_url": original_url, "short_url": short_url},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"short_url": short_url, "error": "Invalid tinyurl"},
                status=status.HTTP_404_NOT_FOUND,
            )
