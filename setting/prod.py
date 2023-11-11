# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tool_master',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# oss 配置
STORAGE_TYPE = 'tencent'
COS_SECRET_ID = 'AKIDsZ1FFJ7hgT0HJ5ctuf7JGyQhmiRxEJL9'
COS_SECRET_KEY = 'nPtBF3cwOp58xXu2uWv54oLeiX7TaTHs'
BUCKET = 'tool-master-1255805830'
ENDPOINT = 'ap-chengdu'
