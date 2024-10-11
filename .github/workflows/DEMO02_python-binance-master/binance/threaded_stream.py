import asyncio  # 导入 asyncio 库，用于异步编程
import threading  # 导入 threading 库，用于多线程编程
from typing import Optional, Dict, Any  # 导入类型提示

from .client import AsyncClient  # 从 client 模块导入异步客户端类
from .helpers import get_loop  # 从 helpers 模块导入获取事件循环的函数

class ThreadedApiManager(threading.Thread):
    """
    线程化的 API 管理器类，负责管理 Binance API 的 WebSocket 连接。
    """
    def __init__(
        self, api_key: Optional[str] = None, api_secret: Optional[str] = None,
        requests_params: Optional[Dict[str, Any]] = None, tld: str = 'com',
        testnet: bool = False, session_params: Optional[Dict[str, Any]] = None
    ):
        """初始化 BinanceSocketManager。

        :param api_key: API 密钥。
        :param api_secret: API 密钥。
        :param requests_params: 请求参数。
        :param tld: 顶级域名。
        :param testnet: 是否使用测试网。
        :param session_params: 会话参数。
        """
        super().__init__()  # 调用父类的初始化方法
        # 获取事件循环，如果没有则创建一个新的事件循环
        self._loop: asyncio.AbstractEventLoop = asyncio.get_event_loop() if asyncio.get_event_loop().is_running() else asyncio.new_event_loop()
        self._client: Optional[AsyncClient] = None  # 初始化异步客户端
        self._running: bool = True  # 运行状态
        self._socket_running: Dict[str, bool] = {}  # 存储每个 WebSocket 的运行状态
        self._client_params = {  # 存储客户端参数
            'api_key': api_key,
            'api_secret': api_secret,
            'requests_params': requests_params,
            'tld': tld,
            'testnet': testnet,
            'session_params': session_params,
        }

    async def _before_socket_listener_start(self):
        """在启动 WebSocket 监听器之前执行的操作。"""
        ...

    async def socket_listener(self):
        """WebSocket 监听器，负责接收消息。"""
        self._client = await AsyncClient.create(loop=self._loop, **self._client_params)  # 创建异步客户端
        await self._before_socket_listener_start()  # 执行启动前的操作
        while self._running:  # 如果运行状态为 True
            await asyncio.sleep(0.2)  # 每 0.2 秒检查一次
        while self._socket_running:  # 如果有 WebSocket 正在运行
            await asyncio.sleep(0.2)  # 每 0.2 秒检查一次

    async def start_listener(self, socket, path: str, callback):
        """启动 WebSocket 监听器。

        :param socket: WebSocket 连接。
        :param path: WebSocket 路径。
        :param callback: 处理消息的回调函数。
        """
        async with socket as s:  # 使用 WebSocket 连接
            while self._socket_running[path]:  # 如果该 WebSocket 正在运行
                try:
                    msg = await asyncio.wait_for(s.recv(), 3)  # 等待接收消息
                except asyncio.TimeoutError:  # 如果超时
                    ...
                    continue  # 继续下一次循环
                else:
                    if not msg:  # 如果没有消息
                        continue  # 继续下一次循环
                    callback(msg)  # 调用回调函数处理消息
        del self._socket_running[path]  # 删除该 WebSocket 的运行状态

    def run(self):
        """线程运行方法，启动 WebSocket 监听器。"""
        self._loop.run_until_complete(self.socket_listener())  # 运行事件循环，直到监听器完成

    def stop_socket(self, socket_name):
        """停止指定的 WebSocket。

        :param socket_name: WebSocket 名称。
        """
        if socket_name in self._socket_running:  # 如果该 WebSocket 存在
            self._socket_running[socket_name] = False  # 设置其运行状态为 False

    async def stop_client(self):
        """停止异步客户端。"""
        if not self._client:  # 如果客户端不存在
            return  # 直接返回
        await self._client.close_connection()  # 关闭客户端连接

    def stop(self):
        """停止线程和异步客户端。"""
        if not self._running:  # 如果运行状态为 False
            return  # 直接返回
        self._running = False  # 设置运行状态为 False
        self._loop.call_soon(asyncio.create_task, self.stop_client())  # 调用停止异步客户端的方法
        for socket_name in self._socket_running.keys():  # 遍历所有 WebSocket
            self._socket_running[socket_name] = False  # 设置其运行状态为 False