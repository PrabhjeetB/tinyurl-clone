from tinyurl.models import TinyUrl
from .redis_utils import RedisUtilities, hash_key


cache = RedisUtilities()


def get_tinyurl(original_url):
    obj = __create_object(original_url)
    return obj.short_url


def __create_object(original_url):
    short_url = hash_key(original_url)
    obj, status = TinyUrl.objects.update_or_create(
        original_url=original_url,
        short_url=short_url,
    )

    max_tries = 1
    while obj.original_url != original_url and max_tries <= 5:
        short_url = hash_key(original_url, offset=max_tries)
        obj, _ = TinyUrl.objects.update_or_create(
            original_url=original_url, short_url=short_url
        )
        print(f"Collision occured, {max_tries} attempts so far.")
        max_tries += 1

    return obj


def get_original_url(short_url):
    url = cache.get(short_url)
    if url:
        return url

    try:
        url = TinyUrl.objects.get(short_url=short_url)
        cache.set(short_url, url.original_url)
        return url.original_url
    except TinyUrl.DoesNotExist:
        return None
