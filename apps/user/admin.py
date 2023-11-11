from django.contrib import admin

from apps.user.models import UserModel


# Register your models here.


@admin.register(UserModel)
class ClassificationAdmin(admin.ModelAdmin):
    """
    导航分类管理
    """
    list_display = ['user_name']
    exclude = ['create_at', 'delete_at']
    list_per_page = 10
