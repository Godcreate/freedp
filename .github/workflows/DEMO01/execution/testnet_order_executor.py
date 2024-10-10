from config.testnet_config import TESTNET_API_KEY, TESTNET_API_SECRET, SYMBOLS
import ccxt

class TestnetOrderExecutor:
    def __init__(self):
        # 初始化Binance测试网交易所对象
        self.exchange = ccxt.binance({
            'apiKey': TESTNET_API_KEY,
            'secret': TESTNET_API_SECRET,
            'enableRateLimit': True,
            'options': {
                'defaultType': 'future',  # 设置为期货交易
                'testnet': True  # 启用测试网
            }
        })

    def place_market_order(self, symbol, side, amount):
        """
        下市价单
        :param symbol: 交易对
        :param side: 买入或卖出
        :param amount: 交易数量
        :return: 订单信息或None（如果下单失败）
        """
        try:
            order = self.exchange.create_market_order(symbol, side, amount)
            return order
        except Exception as e:
            print(f"Error placing testnet market order: {e}")
            return None

    def place_stop_loss_order(self, symbol, side, amount, stop_price):
        """
        设置止损单
        :param symbol: 交易对
        :param side: 买入或卖出
        :param amount: 交易数量
        :param stop_price: 止损价格
        :return: 订单信息或None（如果下单失败）
        """
        try:
            order = self.exchange.create_order(symbol, 'stop_market', side, amount, None, {'stopPrice': stop_price})
            return order
        except Exception as e:
            print(f"Error placing testnet stop loss order: {e}")
            return None

    def place_take_profit_order(self, symbol, side, amount, take_profit_price):
        """
        设置止盈单
        :param symbol: 交易对
        :param side: 买入或卖出
        :param amount: 交易数量
        :param take_profit_price: 止盈价格
        :return: 订单信息或None（如果下单失败）
        """
        try:
            order = self.exchange.create_order(symbol, 'take_profit_market', side, amount, None, {'stopPrice': take_profit_price})
            return order
        except Exception as e:
            print(f"Error placing testnet take profit order: {e}")
            return None

    def get_balance(self, currency='USDT'):
        """
        获取账户余额
        :param currency: 货币类型
        :return: 指定货币的余额或None（如果获取失败）
        """
        try:
            balance = self.exchange.fetch_balance()
            return balance['total'][currency]
        except Exception as e:
            print(f"Error fetching testnet balance: {e}")
            return None