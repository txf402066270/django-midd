__all__ = ["django_response_middleware", "response_data", 'response_codes']


# 中间件配置
# MIDDLEWARE = [
#     ...
#     'django_response_middleware.ResponseMiddleware',
#     ...
# ]

# 如果需要自定义的状态码和message 将response_codes.py文件复制出去
# 在settings.py 定义变量RESPONSE_CODE
# RESPONSE_CODE = '你复制出去response_codes.py的文件的位置'
