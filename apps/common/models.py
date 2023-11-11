from django.db import models
from django.utils import timezone


# Create your models here.

class BaseModel(models.Model):
    """
    基础model,后续所有model都继承此model
    """
    create_at = models.DateTimeField(default=timezone.now, help_text="创建时间", verbose_name="创建时间")
    update_at = models.DateTimeField(default=timezone.now, help_text="更新时间", verbose_name="更新时间")
    delete_at = models.DateTimeField(null=True, blank=True, help_text="删除时间", verbose_name="删除时间")

    class Meta:
        indexes = [
            models.Index(fields=["create_at"], name="create_at_idx"),
            models.Index(fields=["delete_at"], name="delete_at_idx"),
        ]
        abstract = True
