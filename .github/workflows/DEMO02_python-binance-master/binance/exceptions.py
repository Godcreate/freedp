# coding=utf-8
import json

class BinanceAPIException(Exception):
    """自定义异常类，用于处理 Binance API 的错误。"""

    def __init__(self, response, status_code, text):
        self.code = 0
        try:
            json_res = json.loads(text)  # 尝试解析 JSON 错误信息
        except ValueError:
            self.message = 'Invalid JSON error message from Binance: {}'.format(response.text)
        else:
            self.code = json_res.get('code')  # 获取错误代码
            self.message = json_res.get('msg')  # 获取错误信息
        self.status_code = status_code  # HTTP 状态码
        self.response = response  # 响应对象
        self.request = getattr(response, 'request', None)  # 请求对象

    def __str__(self):
        return 'APIError(code=%s): %s' % (self.code, self.message)

class BinanceRequestException(Exception):
    """自定义异常类，用于处理请求错误。"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'BinanceRequestException: %s' % self.message

class BinanceOrderException(Exception):
    """自定义异常类，用于处理订单相关错误。"""

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return 'BinanceOrderException(code=%s): %s' % (self.code, self.message)

class BinanceOrderMinAmountException(BinanceOrderException):
    """自定义异常类，用于处理订单最小数量错误。"""

    def __init__(self, value):
        message = "Amount must be a multiple of %s" % value
        super().__init__(-1013, message)

class BinanceOrderMinPriceException(BinanceOrderException):
    """自定义异常类，用于处理订单最小价格错误。"""

    def __init__(self, value):
        message = "Price must be at least %s" % value
        super().__init__(-1013, message)

class BinanceOrderMinTotalException(BinanceOrderException):
    """自定义异常类，用于处理订单最小总额错误。"""

    def __init__(self, value):
        message = "Total must be at least %s" % value
        super().__init__(-1013, message)

class BinanceOrderUnknownSymbolException(BinanceOrderException):
    """自定义异常类，用于处理未知交易对错误。"""

    def __init__(self, value):
        message = "Unknown symbol %s" % value
        super().__init__(-1013, message)

class BinanceOrderInactiveSymbolException(BinanceOrderException):
    """自定义异常类，用于处理非活跃交易对错误。"""

    def __init__(self, value):
        message = "Attempting to trade an inactive symbol %s" % value
        super().__init__(-1013, message)

class BinanceWebsocketUnableToConnect(Exception):
    """自定义异常类，用于处理 WebSocket 连接失败。"""
    pass

class NotImplementedException(Exception):
    """自定义异常类，用于处理未实现的功能。"""

    def __init__(self, value):
        message = f'Not implemented: {value}'
        super().__init__(message)

class UnknownDateFormat(Exception):
    """自定义异常类，用于处理未知日期格式错误。"""
    ...