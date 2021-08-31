__all__ = ["django_response_middleware", "response_data", 'response_codes']


# 中间件配置
# MIDDLEWARE = [
#     ...
#     自定义状态码 以及返回结果格式化
#     'django_response_middleware.django_response_middleware.ResponseMiddleware',
#     内部报错对外展示的结果
#     'django_response_middleware.django_response_middleware.CustomizeExceptionMiddleware',
#     ...
# ]


# ============如果需要自定义的状态码和message============
# 方法1
# 将response_codes.json文件复制出去
# 在settings.py 定义变量RESPONSE_CODE
# RESPONSE_CODE = '你复制出去response_codes.py的文件的位置'

# 方法2
# 直接使用自定义函数
# customize_code_message

