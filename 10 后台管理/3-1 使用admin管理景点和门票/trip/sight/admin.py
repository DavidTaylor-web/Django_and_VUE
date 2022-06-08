from django.contrib import admin

from sight.models import Sight, Info, Comment, Ticket
from utils.actions import set_invalid, set_valid


@admin.register(Sight)
class SightAdmin(admin.ModelAdmin):
    """ 景点基础信息 """
    list_display = ('name', 'desc', 'main_img', 'score', 'province', 'city',
                    'area', 'town', 'is_valid', 'created_at', 'created_at')
    search_fields = ('name', 'desc')
    list_filter = ('is_top', 'is_hot')
    list_per_page = 20
    actions = [set_invalid, set_valid]


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    """ 景点详细信息 """
    list_display = ('sight', 'entry_explain', 'play_way', 'tips', 'traffic')
    search_fields = ('sight__name', )


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    """ 评论及回复 """
    list_display = ('user', 'sight', 'content', 'score', 'is_top', 'love_count')
    search_fields = ('sight__name', )
    actions = [set_invalid, set_valid]


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    """ 门票管理 """
    list_display = ('sight', 'name', 'types', 'price', 'discount',
                    'total_stock', 'remain_stock', 'is_valid')
    search_fields = ('sight__name', )
    actions = [set_invalid, set_valid]