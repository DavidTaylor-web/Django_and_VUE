from django import template

register = template.Library()


@register.filter
def fmt_uname(value, count=1):
    """
    格式化用户的昵称

    """
    name = value[:count]
    return '{}***'.format(name)

# 方式一：注册过滤器
# register.filter('fmt_name', fmt_uname)
