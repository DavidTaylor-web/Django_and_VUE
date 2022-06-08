from django.contrib import admin
from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ 用户详细信息表 """
    list_display = ('format_username', 'sex', 'age', 'created_at')
    # 每页显示5条数据
    list_per_page = 5
    # 关联的字段一次性查出，减少查询次数
    list_select_related = ('user', )
    # 快捷搜索
    list_filter = ('sex', )
    # 输入内容模糊匹配
    search_fields = ('username', 'user__nickname')

    def format_username(self, obj):
        """ 用户名脱敏处理
        :param obj: Profile
        :return:
        """
        return obj.username[:3] + '***'
    # 修改列名称
    format_username.short_description = '用户名'