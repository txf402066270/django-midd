
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

try:
    from django.conf import settings
    response_code = settings.RESPONSE_CODE
except:
    from .response_codes import response_code


class BaseResponse(object):

    def params_error_response(self, code=None):
        """
        错误返回的结果

        ======== 示例 data有值 ========
        {
            "code": "403.2",
            "message": "禁止访问：请求参数错误！！！",
            "datas": [
                "禁止访问：请求参数错误！！！"
            ]
        }
        """
        if not code:
            code = '403.2'
        code = response_code[code]['code']
        message = response_code[code]['message']
        ret = {'code': code, 'message': message, "datas": [message]}

        return Response(ret)

    def success_response(self, data=None):
        """
        正确返回的结果

        ======== 示例 data有值 ========
        {
            "code": "200",
            "message": "ok",
            "datas": {
                "token": "xx.xxx.xxx",
                "id": 132544,
                "username": "测试代码"
            }
        }

        ======== 示例 data无值 ========
        {
            "code": "200",
            "message": "ok",
            "datas": []
        }
        """

        if response_code['200'].get('datas'):
            del response_code['200']['datas']

        code = response_code['200']['code']
        message = response_code['200']['message']
        if not data:
            ret = {'code': code, 'message': message, 'datas': []}
            return Response(ret)
        else:
            ret = {'code': code, 'message': message, 'datas': data}
            return Response(ret)

    def customize_code_message(self, code, message, data=None):
        """自定义code和message, 不用我默认提供的code和message
            返回的结果样式同上述方法
        """
        if not data:
            data = []
        return Response({'code': code, 'message': message, 'datas': data})


class ResponseApiView(BaseResponse, APIView):
    """配合扩展的父类"""
    pass


class GenericAPIViewResponseApiView(BaseResponse, GenericAPIView):
    """配合扩展的父类"""
    pass
