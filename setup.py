from setuptools import setup, find_packages

setup(name='django-response-mid',
      version='1.02',
      description='django response middleware',
      classifiers=[
          'Programming Language :: Python',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
      ],
      url='https://github.com/txf402066270/django-midd/',
      author='wu-di-tian-ge-ge',
      author_email='402066270@qq.com',
      license='NEU',
      packages=find_packages(),
      zip_safe=True,
      install_requires=['django', 'djangorestframework']
      )
