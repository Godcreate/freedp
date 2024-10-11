from enum import Enum

# 定义交易对类型
SYMBOL_TYPE_SPOT = 'SPOT'

# 定义订单状态
ORDER_STATUS_NEW = 'NEW'
ORDER_STATUS_PARTIALLY_FILLED = 'PARTIALLY_FILLED'
ORDER_STATUS_FILLED = 'FILLED'
ORDER_STATUS_CANCELED = 'CANCELED'
ORDER_STATUS_PENDING_CANCEL = 'PENDING_CANCEL'
ORDER_STATUS_REJECTED = 'REJECTED'
ORDER_STATUS_EXPIRED = 'EXPIRED'

# 定义 K 线时间间隔
KLINE_INTERVAL_1SECOND = '1s'
KLINE_INTERVAL_1MINUTE = '1m'
KLINE_INTERVAL_3MINUTE = '3m'
KLINE_INTERVAL_5MINUTE = '5m'
KLINE_INTERVAL_15MINUTE = '15m'
KLINE_INTERVAL_30MINUTE = '30m'
KLINE_INTERVAL_1HOUR = '1h'
KLINE_INTERVAL_2HOUR = '2h'
KLINE_INTERVAL_4HOUR = '4h'
KLINE_INTERVAL_6HOUR = '6h'
KLINE_INTERVAL_8HOUR = '8h'
KLINE_INTERVAL_12HOUR = '12h'
KLINE_INTERVAL_1DAY = '1d'
KLINE_INTERVAL_3DAY = '3d'
KLINE_INTERVAL_1WEEK = '1w'
KLINE_INTERVAL_1MONTH = '1M'

# 定义交易方向
SIDE_BUY = 'BUY'
SIDE_SELL = 'SELL'

# 定义订单类型
ORDER_TYPE_LIMIT = 'LIMIT'
ORDER_TYPE_MARKET = 'MARKET'
ORDER_TYPE_STOP_LOSS = 'STOP_LOSS'
ORDER_TYPE_STOP_LOSS_LIMIT = 'STOP_LOSS_LIMIT'
ORDER_TYPE_TAKE_PROFIT = 'TAKE_PROFIT'
ORDER_TYPE_TAKE_PROFIT_LIMIT = 'TAKE_PROFIT_LIMIT'
ORDER_TYPE_LIMIT_MAKER = 'LIMIT_MAKER'

# 定义期货订单类型
FUTURE_ORDER_TYPE_LIMIT = 'LIMIT'
FUTURE_ORDER_TYPE_MARKET = 'MARKET'
FUTURE_ORDER_TYPE_STOP = 'STOP'
FUTURE_ORDER_TYPE_STOP_MARKET = 'STOP_MARKET'
FUTURE_ORDER_TYPE_TAKE_PROFIT = 'TAKE_PROFIT'
FUTURE_ORDER_TYPE_TAKE_PROFIT_MARKET = 'TAKE_PROFIT_MARKET'
FUTURE_ORDER_TYPE_LIMIT_MAKER = 'LIMIT_MAKER'
FUTURE_ORDER_TYPE_TRAILING_STOP_MARKET = 'TRAILING_STOP_MARKET'

# 定义有效时间类型
TIME_IN_FORCE_GTC = 'GTC'  # 直到取消
TIME_IN_FORCE_IOC = 'IOC'  # 立即成交或取消
TIME_IN_FORCE_FOK = 'FOK'  # 全部成交或取消
TIME_IN_FORCE_GTX = 'GTX'  # 仅限挂单

# 定义订单响应类型
ORDER_RESP_TYPE_ACK = 'ACK'
ORDER_RESP_TYPE_RESULT = 'RESULT'
ORDER_RESP_TYPE_FULL = 'FULL'

# 定义深度数据类型
WEBSOCKET_DEPTH_5 = '5'
WEBSOCKET_DEPTH_10 = '10'
WEBSOCKET_DEPTH_20 = '20'

# 定义其他类型
NO_SIDE_EFFECT_TYPE = 'NO_SIDE_EFFECT'
MARGIN_BUY_TYPE = 'MARGIN_BUY'
AUTO_REPAY_TYPE = 'AUTO_REPAY'

# 定义历史 K 线类型
class HistoricalKlinesType(Enum):
    SPOT = 1
    FUTURES = 2
    FUTURES_COIN = 3

# 定义期货类型
class FuturesType(Enum):
    USD_M = 1
    COIN_M = 2

# 定义合约类型
class ContractType(Enum):
    PERPETUAL = "perpetual"
    CURRENT_QUARTER = "current_quarter"
    NEXT_QUARTER = "next_quarter"