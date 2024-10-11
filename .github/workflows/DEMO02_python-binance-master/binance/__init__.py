"""An unofficial Python wrapper for the Binance exchange API v3

.. moduleauthor:: Sam McHardy

"""

# 定义包的版本号
__version__ = "1.0.19"

# 从其他模块导入主要的类,使它们可以直接从binance包中导入
from binance.client import Client, AsyncClient  # noqa
from binance.depthcache import DepthCacheManager, OptionsDepthCacheManager, ThreadedDepthCacheManager  # noqa
from binance.streams import BinanceSocketManager, ThreadedWebsocketManager  # noqa
