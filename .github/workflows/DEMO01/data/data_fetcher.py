import ccxt
import pandas as pd
from config.config import API_KEY, API_SECRET, SYMBOL, TIMEFRAME

class DataFetcher:
    def __init__(self):
        # 初始化交易所对象
        self.exchange = ccxt.binance({
            'apiKey': API_KEY,
            'secret': API_SECRET,
            'enableRateLimit': True,
            'options': {'defaultType': 'future'}
        })

    def get_historical_data(self, limit=100):
        """
        获取历史K线数据
        :param limit: 获取的K线数量
        :return: 包含历史数据的DataFrame
        """
        ohlcv = self.exchange.fetch_ohlcv(SYMBOL, TIMEFRAME, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df

    def get_latest_price(self):
        """
        获取最新价格
        :return: 最新价格
        """
        ticker = self.exchange.fetch_ticker(SYMBOL)
        return ticker['last']