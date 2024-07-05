# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "tool_master",
        "USER": "postgres",
        "PASSWORD": "root",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

# 密码加盐
PWD_SALT = "12335"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# oss 配置
STORAGE_TYPE = "tencent"
COS_SECRET_ID = ""
COS_SECRET_KEY = ""
BUCKET = "tool-master-1255805830"
ENDPOINT = "ap-chengdu"
