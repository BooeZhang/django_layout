from django.db import models

from apps.common.models import BaseModel


# Create your models here.
class UserModel(BaseModel):
    """
    用户
    """
    user_name = models.CharField(null=True, max_length=50, help_text="用户名", verbose_name="用户名")
    password = models.CharField(null=True, max_length=50, help_text="密码", verbose_name="密码")
    remark = models.CharField(max_length=255, help_text="备注", verbose_name="备注")
    header_img = models.CharField(max_length=1024, help_text="头像url", verbose_name="头像url")
    is_super = models.BooleanField(default=False, help_text="是否是超级用户 0:不是 1:是", verbose_name="是否是超级用户 0:不是 1:是")
    is_active = models.BooleanField(default=True, help_text="是否是激活状态 0:不是 1:是", verbose_name="是否是激活状态 0:不是 1:是")

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
