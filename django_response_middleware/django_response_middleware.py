import logging
import json
from django.http.response import HttpResponse

from django_response_middleware.utils.type_conversion import list_str

logger = logging.getLogger(__name__)


class MyBaseMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response


class ResponseMiddleware(MyBaseMiddleware):
    """自定义返回结果"""

    def process_template_response(self, request, response):

        if hasattr(response, 'data'):
            # ============  返回详情  ============
            # {
            #     "code": "200",
            #     "message": "ok",
            #     "datas": { ... }
            # ============
            if response.status_code == 200:
                if 'datas' not in response.data and 'code' not in response.data:
                    data = response.data
                    del response.data
                    response.data = {
                        'code': '{}'.format(response.status_code),
                        'message': 'ok',
                        'datas': data
                    }

            else:
                # django抛出的异常 如dfr序列化器反序列化异常
                # data = 错误的具体信息

                # ============  返回详情  ============
                # {
                #     "code": "400",
                #     "message": "error",
                #     "datas": {
                #         "authentication_error": [
                #             {
                #                 "date": "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
                #             },
                #             {
                #                 "total_amount": "This field is required."
                #             }
                #         ]
                #     }
                # }
                # ============
                response.status_code = 200
                data = response.data
                del response.data
                response.data = {
                    'code': '400',
                    'message': 'error',
                    'datas': {'authentication_error': list_str(data)},
                }

        return response


class CustomizeExceptionMiddleware(MyBaseMiddleware):
    """服务器异常不对外爆露，使用自定义"""

    def process_exception(self, request, exception):

        logger.error({'process_exception捕获异常': exception})

        return HttpResponse(
            json.dumps({'code': '06537',
                        'message': 'server_error',
                        'datas': {"error_info": {'error_info': '请联系无敌后台哥哥(姐姐)解决!!'}}
                        }),
            content_type="application/json")
