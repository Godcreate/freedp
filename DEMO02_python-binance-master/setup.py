#!/usr/bin/env python
# 指定脚本的解释器为 Python

from setuptools import setup  # 从 setuptools 模块导入 setup 函数
import codecs  # 导入 codecs 模块，用于处理文件编码
import os  # 导入 os 模块，用于与操作系统交互
import re  # 导入 re 模块，用于正则表达式操作

# 打开 binance/__init__.py 文件以读取版本信息
with codecs.open(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),  # 获取当前文件目录的绝对路径
            'binance',  # 指定子目录 'binance'
            '__init__.py'  # 指定要打开的文件
        ), 'r', 'latin1') as fp:  # 以 'latin1' 编码读取文件
    try:
        # 使用正则表达式查找版本号
        version = re.findall(r'^__version__ = "([^"]+)"\r?$', fp.read(), re.M)[0]
    except IndexError:
        # 如果未找到版本号，抛出运行时错误
        raise RuntimeError('Unable to determine version.')

# 读取 README 文件以获取长描述
with open("README.rst", "r") as fh:
    long_description = fh.read()  # 读取文件内容

# 调用 setup 函数配置包的元数据
setup(
    name='python-binance',  # 包的名称
    version=version,  # 包的版本
    packages=['binance'],  # 包含的模块
    description='Binance REST API python implementation',  # 简短描述
    long_description=long_description,  # 长描述
    long_description_content_type="text/x-rst",  # 长描述的内容类型
    url='https://github.com/sammchardy/python-binance',  # 项目的 URL
    author='Sam McHardy',  # 作者名称
    license='MIT',  # 许可证类型
    author_email='',  # 作者电子邮件（留空）
    install_requires=[  # 依赖的包
        'requests', 'six', 'dateparser', 'aiohttp', 'ujson', 'websockets', 'pycryptodome'
    ],
    keywords='binance exchange rest api bitcoin ethereum btc eth neo',  # 关键字
    classifiers=[  # 分类器，用于描述包的特性
        'Intended Audience :: Developers',  # 目标受众
        'License :: OSI Approved :: MIT License',  # 许可证信息
        'Operating System :: OS Independent',  # 操作系统兼容性
        'Programming Language :: Python :: 3',  # 支持的 Python 版本
        'Programming Language :: Python :: 3.5',  # 支持的 Python 版本
        'Programming Language :: Python :: 3.6',  # 支持的 Python 版本
        'Programming Language :: Python :: 3.7',  # 支持的 Python 版本
        'Programming Language :: Python',  # 支持的编程语言
        'Topic :: Software Development :: Libraries :: Python Modules',  # 主题分类
    ],
)
