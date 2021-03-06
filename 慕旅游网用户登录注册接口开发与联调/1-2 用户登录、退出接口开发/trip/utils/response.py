from django.http import JsonResponse


class NotFoundJsonResponse(JsonResponse):
    """ 400 对应JSON响应 """
    status_code = 400

    def __init__(self, *args, **kwargs):

        data = {
            "error_code": "404000",
            "error_msg": "您访问的内容不存在或已被删除。"
        }
        super().__init__(data, *args, **kwargs)


class BadRequestJsonResponse(JsonResponse):
    """ 表单请求验证没有通过，错误显示 """
    status_code = 400

    def __init__(self, err_list=[], *args, **kwargs):
        data = {
            "error_code": "400000",
            "error_msg": "参数格式不正确",
            "error_list": err_list
        }
        super().__init__(data, *args, **kwargs)


class MethodNotAllowedJsonResponse(JsonResponse):
    """ 请求方式不被允许 """
    status_code = 405

    def __init__(self, *args, **kwargs):
        data = {
            "error_code": "405000",
            "error_msg": "请求方式不被允许",
        }
        super().__init__(data, *args, **kwargs)