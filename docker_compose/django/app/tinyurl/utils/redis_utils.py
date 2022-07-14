import hashlib
import os

import redis


REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")


def hash_key(original_url, offset=0):
    """
    Generate md5 hash for the given URL.

    Args:
        original_url (str): Original url to be shortened.
        offset (int): Offset for substring selection.

    Returns:
        str: 6 digit unqiue hash.
    """
    md5hash = hashlib.md5(original_url.encode("utf-8")).hexdigest()
    short_url = md5hash[offset : 6 + offset]
    return short_url


class RedisUtilities:
    """
    Redis utility to add, update, get and delete objects in redis cache.
    """

    def __init__(self):
        self.redis_client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            health_check_interval=5,
            socket_connect_timeout=1,
        )

    def set(self, original_url):
        """
        Add/update key:value pair in redis server cache.

        Args:
            key (str): Custom hash generated for input using __hash_key().
            original_url (str): Original url to be shortened.
        """
        short_url = hash_key(original_url)
        try:
            self.redis_client.set(short_url, original_url)

        except Exception as e:
            print(f"Redis error: {str(e)}")

    def get(self, short_url):
        """
        Get output for a cached input if available.

        Args:
            short_url: Shortened URL.

        Returns:
            str/None: Original URL for the given shortened URL, else None.
        """
        try:
            res = self.redis_client.get(short_url)
            if not res:
                return None
            else:
                return res

        except Exception as e:
            print(f"Redis error: {str(e)}")
            return None
