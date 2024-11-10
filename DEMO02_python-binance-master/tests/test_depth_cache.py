from binance.depthcache import DepthCache  # 导入深度缓存类
from decimal import Decimal  # 导入 Decimal 类型
import pytest  # 导入 pytest 测试框架

TEST_SYMBOL = "BNBBTC"  # 测试用的交易对


@pytest.fixture  # pytest 的固定装置
def fresh_cache():  # 定义一个新的深度缓存
    return DepthCache(TEST_SYMBOL, Decimal)  # 返回深度缓存实例


def test_add_bids(fresh_cache):  # 测试添加买单的功能
    """Verify basic functionality for adding a bid to the cache"""  # 测试文档字符串
    high_bid = [0.111, 489]  # 高买单
    mid_bid = [0.018, 300]  # 中等买单
    low_bid = [0.001, 100]  # 低买单
    for bid in [high_bid, low_bid, mid_bid]:  # 循环添加买单
        fresh_cache.add_bid(bid)  # 添加买单到缓存

    bids = fresh_cache.get_bids()  # 获取当前的买单列表

    assert len(bids) == 3  # 断言买单数量为 3

    assert bids == sorted(bids, reverse=True)  # 断言买单按价格降序排列

    assert isinstance(bids[0][0], Decimal)  # 断言最高买单价格为 Decimal 类型
    assert isinstance(bids[0][1], Decimal)  # 断言最高买单数量为 Decimal 类型


def test_add_asks(fresh_cache):  # 测试添加卖单的功能
    """Verify basic functionality for adding an ask to the cache"""  # 测试文档字符串
    high_ask = [0.111, 489]  # 高卖单
    mid_ask = [0.018, 300]  # 中等卖单
    low_ask = [0.001, 100]  # 低卖单

    for ask in [high_ask, low_ask, mid_ask]:  # 循环添加卖单
        fresh_cache.add_ask(ask)  # 添加卖单到缓存

    asks = fresh_cache.get_asks()  # 获取当前的卖单列表

    # 三个卖单应该在缓存中
    assert len(asks) == 3  # 断言卖单数量为 3

    # 最低卖单价格应该是第一个（升序排列）
    assert asks == sorted(asks)  # 断言卖单按价格升序排列

    assert isinstance(asks[0][0], Decimal)  # 断言最低卖单价格为 Decimal 类型
    assert isinstance(asks[0][1], Decimal)  # 断言最低卖单数量为 Decimal 类型