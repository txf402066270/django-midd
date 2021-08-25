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
#     'django_response_middleware.django_response_middleware.ResponseMiddleware',
#     ...
# ]
```


# 2 自定义状态码
## 使用方法
```python
# 1 如果需要自定义的状态码和message 将response_codes.json文件复制出去放到你自己的目录
# 2 在settings.py 定义变量RESPONSE_CODE
# 3 with open(BASE_DIR + r'你自己的目录/response_codes.json', 'r', encoding='utf-8') as f:
#    RESPONSE_CODE = json.loads(f.read())

# 4 以下导包三选一 具体参数到response_data查看
# 5 前端检测我们自定义的code即可

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


### 3 备注
因为django自己的返回结果和我们代码写的结构有时候不一样，
导致前端的同修的工作量很大，
为了提高工作效率特意增加此方法

