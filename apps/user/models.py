from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User

from apps.common.models import BaseModel


# Create your models here.
class UserModel(BaseModel):
    """
    用户
    """

    user_name = models.CharField(
        max_length=50, unique=True, help_text="用户名", verbose_name="用户名"
    )
    password = models.CharField(max_length=255, help_text="密码", verbose_name="密码")
    remark = models.CharField(
        blank=True, max_length=255, help_text="备注", verbose_name="备注"
    )
    header_img = models.CharField(
        blank=True, max_length=1024, help_text="头像url", verbose_name="头像url"
    )
    is_super = models.BooleanField(
        default=False,
        help_text="是否是超级用户 0:不是 1:是",
        verbose_name="是否是超级用户 0:不是 1:是",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="是否是激活状态 0:不是 1:是",
        verbose_name="是否是激活状态 0:不是 1:是",
    )

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.password = make_password(self.password, settings.PWD_SALT, "pbkdf2_sha256")
        super(UserModel, self).save(*args, **kwargs)

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
