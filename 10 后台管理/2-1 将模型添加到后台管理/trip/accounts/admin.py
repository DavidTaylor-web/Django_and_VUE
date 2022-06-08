from django.contrib import admin
from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ 用户详细信息表 """
    list_display = ('username', 'sex', 'age', 'created_at')