#!/usr/bin/env python
# coding=utf-8

from binance.client import Client
import pytest
import requests_mock


client = Client("api_key", "api_secret")


def test_exact_amount():
    """Test Exact amount returned"""

    first_available_res = [
        [
            1500004800000,
            "0.00005000",
            "0.00005300",
            "0.00001000",
            "0.00004790",
            "663152.00000000",
            1500004859999,
            "30.55108144",
            43,
            "559224.00000000",
            "25.65468144",
            "83431971.04346950",
        ]
    ]

    first_res = []
    row = [
        1519892340000,
        "0.00099400",
        "0.00099810",
        "0.00099400",
        "0.00099810",
        "4806.04000000",
        1519892399999,
        "4.78553253",
        154,
        "1785.14000000",
        "1.77837524",
        "0",
    ]

    for i in range(0, 500):
        first_res.append(row)

    second_res = []

    with requests_mock.mock() as m:
        m.get(
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC",
            json=first_available_res,
        )
        m.get(
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1000&startTime=1519862400000&symbol=BNBBTC",
            json=first_res,
        )
        m.get(
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1000&startTime=1519892400000&symbol=BNBBTC",
            json=second_res,
        )
        klines = client.get_historical_klines(
            symbol="BNBBTC", interval=Client.KLINE_INTERVAL_1MINUTE, start_str="1st March 2018"
        )
        assert len(klines) == 500


def test_start_and_end_str():
    """Test start_str and end_str work correctly with string"""

    first_available_res = [
        [
            1500004800000,
            "0.00005000",
            "0.00005300",
            "0.00001000",
            "0.00004790",
            "663152.00000000",
            1500004859999,
            "30.55108144",
            43,
            "559224.00000000",
            "25.65468144",
            "83431971.04346950",
        ]
    ]
    first_res = []
    row = [
        1519892340000,
        "0.00099400",
        "0.00099810",
        "0.00099400",
        "0.00099810",
        "4806.04000000",
        1519892399999,
        "4.78553253",
        154,
        "1785.14000000",
        "1.77837524",
        "0",
    ]

    for i in range(0, 300):
        first_res.append(row)

    with requests_mock.mock() as m:
        m.get(
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC",
            json=first_available_res,
        )
        m.get(
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1000&startTime=1519862400000&endTime=1519880400000&symbol=BNBBTC",
            json=first_res,
        )
        klines = client.get_historical_klines(
            symbol="BNBBTC",
            interval=Client.KLINE_INTERVAL_1MINUTE,
            start_str="1st March 2018",
            end_str="1st March 2018 05:00:00",
        )
        assert len(klines) == 300


def test_start_and_end_timestamp():
    """Test start_str and end_str work correctly with integer timestamp"""

    first_available_res = [
        [
            1500004800000,
            "0.00005000",
            "0.00005300",
            "0.00001000",
            "0.00004790",
            "663152.00000000",
            1500004859999,
            "30.55108144",
            43,
            "559224.00000000",
            "25.65468144",
            "83431971.04346950",
        ]
    ]
    first_res = []
    row = [
        1519892340000,
        "0.00099400",
        "0.00099810",
        "0.00099400",
        "0.00099810",
        "4806.04000000",
        1519892399999,
        "4.78553253",
        154,
        "1785.14000000",
        "1.77837524",
        "0",
    ]

    for i in range(0, 300):
        first_res.append(row)

    with requests_mock.mock() as m:
        m.get(
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC",
            json=first_available_res,
        )
        m.get(
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1000&startTime=1519862400000&endTime=1519880400000&symbol=BNBBTC",
            json=first_res,
        )
        klines = client.get_historical_klines(
            symbol="BNBBTC",
            interval=Client.KLINE_INTERVAL_1MINUTE,
            start_str=1519862400000,
            end_str=1519880400000,
        )
        assert len(klines) == 300


def test_historical_kline_generator():
    """Test kline historical generator"""

    first_available_res = [
        [
            1500004800000,
            "0.00005000",
            "0.00005300",
            "0.00001000",
            "0.00004790",
            "663152.00000000",
            1500004859999,
            "30.55108144",
            43,
            "559224.00000000",
            "25.65468144",
            "83431971.04346950",
        ]
    ]
    first_res = []
    row = [
        1519892340000,
        "0.00099400",
        "0.00099810",
        "0.00099400",
        "0.00099810",
        "4806.04000000",
        1519892399999,
        "4.78553253",
        154,
        "1785.14000000",
        "1.77837524",
        "0",
    ]

    for i in range(0, 300):
        first_res.append(row)

    with requests_mock.mock() as m:
        m.get(
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC",
            json=first_available_res,
        )
        m.get(
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1000&startTime=1519862400000&endTime=1519880400000&symbol=BNBBTC",
            json=first_res,
        )
        klines = client.get_historical_klines_generator(
            symbol="BNBBTC",
            interval=Client.KLINE_INTERVAL_1MINUTE,
            start_str=1519862400000,
            end_str=1519880400000,
        )

        for i in range(300):
            assert len(next(klines)) > 0

        with pytest.raises(StopIteration):
            next(klines)


def test_historical_kline_generator_empty_response():
    """Test kline historical generator if an empty list is returned from API"""
    first_available_res = [
        [
            1500004800000,
            "0.00005000",
            "0.00005300",
            "0.00001000",
            "0.00004790",
            "663152.00000000",
            1500004859999,
            "30.55108144",
            43,
            "559224.00000000",
            "25.65468144",
            "83431971.04346950",
        ]
    ]
    first_res = []

    with requests_mock.mock() as m:
        m.get(
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC",
            json=first_available_res,
        )
        m.get(
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1000&startTime=1519862400000&endTime=1519880400000&symbol=BNBBTC",
            json=first_res,
        )
        klines = client.get_historical_klines_generator(
            symbol="BNBBTC",
            interval=Client.KLINE_INTERVAL_1MINUTE,
            start_str=1519862400000,
            end_str=1519880400000,
        )

        with pytest.raises(StopIteration):
            next(klines)

def test_start_and_limit():  # 测试开始和限制
    """Test start_str and limit work correctly with integer timestamp"""  # 测试文档字符串
 
    first_available_res = [  # 模拟第一个可用的响应
        [
            1500004800000,  # 时间戳
            "0.00005000",  # 开盘价
            "0.00005300",  # 最高价
            "0.00001000",  # 最低价
            "0.00004790",  # 收盘价
            "663152.00000000",  # 成交量
            1500004859999,  # 结束时间戳
            "30.55108144",  # 成交额
            43,  # 交易次数
            "559224.00000000",  # 成交额
            "25.65468144",  # 成交额
            "83431971.04346950",  # 成交额
        ]
    ]
    first_res = []  # 初始化第一个响应
    row = [  # 模拟每一行的 K 线数据
        1519892340000,  # 时间戳
        "0.00099400",  # 开盘价
        "0.00099810",  # 最高价
        "0.00099400",  # 最低价
        "0.00099810",  # 收盘价
        "4806.04000000",  # 成交量
        1519892399999,  # 结束时间戳
        "4.78553253",  # 成交额
        154,  # 交易次数
        "1785.14000000",  # 成交额
        "1.77837524",  # 成交额
        "0",  # 成交额
    ]
 
    for i in range(0, 5):  # 循环添加 5 行数据
        first_res.append(row)  # 将行数据添加到响应中
 
    with requests_mock.mock() as m:  # 使用 requests_mock 模拟 HTTP 请求
        m.get(  # 模拟 GET 请求
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC",
            json=first_available_res,  # 返回第一个可用的响应
        )
        m.get(  # 模拟 GET 请求
            "https://api.binance.com/api/v3/klines?interval=1m&limit=5&startTime=1519892400000&symbol=BNBBTC",
            json=first_res,  # 返回第一个响应
        )
        m.get(  # 模拟 GET 请求
            "https://api.binance.com/api/v3/klines?interval=1m&limit=5&startTime=1519862400000&symbol=BNBBTC",
            json=first_res,  # 返回第一个响应
        )
        klines = client.get_historical_klines(  # 调用获取历史 K 线的方法
            symbol="BNBBTC",
            interval=Client.KLINE_INTERVAL_1MINUTE,
            start_str=1519862400000,  # 设置开始时间戳
            limit=5,  # 设置限制为 5
        )
        assert len(klines) == 5  # 断言返回的 K 线数量为 5