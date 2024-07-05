from django.contrib import admin

from apps.user.models import UserModel


# Register your models here.


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    """用户管理"""

    list_display = ["user_name", "header_img", "is_super", "is_active", "create_at"]
    exclude = ["delete_at"]
    list_per_page = 10
