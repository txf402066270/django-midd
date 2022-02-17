# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(name='django-response-mid', # 名字
      version='2.10',  # 版本
      description='django response middleware',  # 简介一般我们放在readme.md
      classifiers=[
          'Programming Language :: Python',  # python
          'Intended Audience :: Developers',  # 受众人
          'Operating System :: OS Independent',  # 系统
      ],
      url='https://github.com/txf402066270/django-midd/',  # git的目录
      author='wu-di-tian-ge-ge',  # 作者
      author_email='402066270@qq.com', # 邮箱方便交流
      license='NEU',  #
      packages=find_packages(),  # 默认
      zip_safe=True,  # 默认
      install_requires=['django', 'djangorestframework']  # 需要的包
      )