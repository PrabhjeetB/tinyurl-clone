from rest_framework import serializers

from tinyurl.models import TinyUrl


class OriginalUrlSerializer(serializers.ModelSerializer):
    """
    Serializer for original Url.
    """

    class Meta:
        model = TinyUrl
        fields = ("original_url",)


class TinyUrlSerializer(serializers.ModelSerializer):
    """
    Serializer for TinyUrl objects.
    """

    class Meta:
        model = TinyUrl
        fields = ("short_url",)
