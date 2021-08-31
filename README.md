# 0 安装
``` python
pip install django-response-mid
```

# 1 自定义中间件

### settings.py 配置
```python
# 1 中间件配置
# 2 response.status_code会强制变为200无论失败与否
# 3 返回结果样式查看2自定义状态码 
# MIDDLEWARE = [
#     ...
#     自定义状态码 以及返回结果格式化
#     'django_response_middleware.django_response_middleware.ResponseMiddleware',
#     内部报错对外展示的结果
#     'django_response_middleware.django_response_middleware.CustomizeExceptionMiddleware',
#     ...]
#   
```


# 2 自定义状态码
## 使用方法
```python

# ============如果需要自定义的状态码和message============
# 方法1 
# 将response_codes.json文件复制出去
# 在settings.py 定义变量RESPONSE_CODE
# RESPONSE_CODE = '你复制出去response_codes.py的文件的位置'

# 方法2
# 直接使用自定义函数
# customize_code_message

# 以下导包三选一 具体参数到response_data查看
# 前端检测我们自定义的code即可

from django_response_middleware.response_data import BaseResponse
from django_response_middleware.response_data import ResponseApiView
from django_response_middleware.response_data import GenericAPIViewResponseApiView

class CaseStudyView(ResponseApiView):
   
    def post(self, request):
        data = {'id': 666}
        return self.success_response(data)
    # 案例1 正常返回
    # {
    #  "code": "200",
    #  "message": "ok",
    #  "datas": {
    #            'id':666
    #             }
    #  }


    def get(self, request):
        pass
        return self.params_error_response()
    # 案例2 错误返回
    # {
    #  "code": "403.2",
    #  "message": "禁止访问：请求参数错误！！！",
    #  "datas": [
    #      "禁止访问：请求参数错误！！！"
    #        ]
    # }

    def put(self, request):
        pass
        return self.params_error_response('自定义状态码')
    
    # 案例3 自定义错误返回
    # {
    #  "code": "自定义状态码",
    #  "message": "自定义错误信息",
    #  "datas": [
    #      "自定义错误信息"
    #        ]
    # }
    
    def delete(self, request):
        pass
        return self.success_response()
    
    # 案例4 系统错误返回
    # {
    #  "code": "400",
    #  "message": "error",
    #  "datas": [
    #      "系统返回的错误信息key": "系统返回的错误信息value"
    #        ]
    # }
```

### response_data.py 新增
```python
def customize_code_message(self, code, message, data=None):
    """自定义code和message, 不用我默认提供的code和message
        返回的结果样式同上
    """
    pass

```

### django_response_middleware.py 新增
```python
class CustomizeExceptionMiddleware(MyBaseMiddleware):
    """服务器异常不对外爆露，使用自定义"""

    def process_exception(self, request, exception):

        logger.error({'process_exception捕获异常': exception})

        return HttpResponse(
            json.dumps({'code': '06537',
                        'message': 'error',
                        'datas': {'info': '请联系无敌后台哥哥(姐姐)解决!!'}
                        }),
            content_type="application/json")


### 3 备注
因为django自己的返回结果和我们代码写的结构有时候不一样，
导致前端的同修的工作量很大，
为了提高工作效率特意增加此方法

