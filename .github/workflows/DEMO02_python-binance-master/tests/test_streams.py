from binance.streams import BinanceSocketManager  # 导入 BinanceSocketManager 类
from binance.client import AsyncClient  # 导入异步客户端类
import pytest  # 导入 pytest 测试框架


@pytest.mark.asyncio  # 标记该测试为异步测试
async def test_socket_stopped_on_aexit():  # 定义测试函数
    """测试在异步上下文管理器退出时是否正确停止WebSocket连接"""  # 测试文档字符串
    
    # 创建异步客户端
    client = AsyncClient()  # 实例化异步客户端
    # 创建WebSocket管理器
    bm = BinanceSocketManager(client)  # 实例化 WebSocket 管理器
    
    # 创建第一个交易WebSocket
    ts1 = bm.trade_socket('BNBBTC')  # 创建交易 WebSocket
    async with ts1:  # 使用异步上下文管理器
        pass  # 在上下文管理器中不做任何操作
    
    # 创建第二个交易WebSocket
    ts2 = bm.trade_socket('BNBBTC')  # 创建第二个交易 WebSocket
    
    # 验证第二个WebSocket不是第一个,确保第一个已被移除
    assert ts2 is not ts1, "socket should be removed from _conn on exit"  # 断言第二个 WebSocket 与第一个不同
    
    # 关闭异步客户端连接
    await client.close_connection()  # 关闭异步客户端连接