from config.testnet_config import SYMBOLS, POSITION_SIZE, BTC_STOP_LOSS_PERCENTAGE, BTC_TAKE_PROFIT_PERCENTAGE, ETH_STOP_LOSS_PERCENTAGE, ETH_TAKE_PROFIT_PERCENTAGE

class MultiStrategy:
    def __init__(self, order_executor):
        self.order_executor = order_executor
        self.strategies = {
            'BTC/USDT': {
                'side': 'buy',
                'stop_loss': BTC_STOP_LOSS_PERCENTAGE,
                'take_profit': BTC_TAKE_PROFIT_PERCENTAGE
            },
            'ETH/USDT': {
                'side': 'sell',
                'stop_loss': ETH_STOP_LOSS_PERCENTAGE,
                'take_profit': ETH_TAKE_PROFIT_PERCENTAGE
            }
        }

    def execute_strategies(self):
        """
        执行所有交易策略
        """
        for symbol, strategy in self.strategies.items():
            self.execute_single_strategy(symbol, strategy)

    def execute_single_strategy(self, symbol, strategy):
        """
        执行单个交易策略
        :param symbol: 交易对
        :param strategy: 策略参数
        """
        # 获取当前市场价格
        ticker = self.order_executor.exchange.fetch_ticker(symbol)
        current_price = ticker['last']

        # 计算交易数量
        amount = POSITION_SIZE / current_price

        # 下市价单
        order = self.order_executor.place_market_order(symbol, strategy['side'], amount)
        if order:
            print(f"Placed {strategy['side']} order for {symbol}: {order}")

            # 设置止损
            stop_loss_price = self.calculate_stop_loss(current_price, strategy['stop_loss'], strategy['side'])
            stop_loss_side = 'buy' if strategy['side'] == 'sell' else 'sell'
            stop_loss_order = self.order_executor.place_stop_loss_order(symbol, stop_loss_side, amount, stop_loss_price)
            print(f"Placed stop loss order for {symbol}: {stop_loss_order}")

            # 设置止盈
            take_profit_price = self.calculate_take_profit(current_price, strategy['take_profit'], strategy['side'])
            take_profit_side = 'buy' if strategy['side'] == 'sell' else 'sell'
            take_profit_order = self.order_executor.place_take_profit_order(symbol, take_profit_side, amount, take_profit_price)
            print(f"Placed take profit order for {symbol}: {take_profit_order}")

    def calculate_stop_loss(self, current_price, percentage, side):
        """
        计算止损价格
        :param current_price: 当前价格
        :param percentage: 止损百分比
        :param side: 交易方向
        :return: 止损价格
        """
        if side == 'buy':
            return current_price * (1 - percentage)
        else:
            return current_price * (1 + percentage)

    def calculate_take_profit(self, current_price, percentage, side):
        """
        计算止盈价格
        :param current_price: 当前价格
        :param percentage: 止盈百分比
        :param side: 交易方向
        :return: 止盈价格
        """
        if side == 'buy':
            return current_price * (1 + percentage)
        else:
            return current_price * (1 - percentage)