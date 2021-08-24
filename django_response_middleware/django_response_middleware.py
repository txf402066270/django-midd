class ResponseMiddleware(object):
    """自定义返回结果"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if hasattr(response, 'data'):

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
                response.status_code = 200
                data = response.data
                del response.data
                response.data = {
                    'code': '400',
                    'message': 'error',
                    'datas': data,
                }

        return response
