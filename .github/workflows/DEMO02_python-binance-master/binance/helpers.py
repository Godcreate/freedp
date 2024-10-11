import asyncio
from decimal import Decimal
from typing import Union, Optional, Dict

import dateparser
import pytz

from datetime import datetime

from binance.exceptions import UnknownDateFormat


def date_to_milliseconds(date_str: str) -> int:
    """将可读日期字符串转换为毫秒时间戳。

    :param date_str: 可读格式的日期字符串。
    :return: 转换后的毫秒时间戳。
    """
    # 获取 UTC 的纪元值
    epoch: datetime = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)
    # 解析日期字符串
    d: Optional[datetime] = dateparser.parse(date_str, settings={"TIMEZONE": "UTC"})
    if not d:
        raise UnknownDateFormat(date_str)  # 如果解析失败，抛出异常

    # 如果日期没有时区信息，则应用 UTC 时区
    if d.tzinfo is None or d.tzinfo.utcoffset(d) is None:
        d = d.replace(tzinfo=pytz.utc)

    # 返回时间差的毫秒数
    return int((d - epoch).total_seconds() * 1000.0)


def interval_to_milliseconds(interval: str) -> Optional[int]:
    """将 Binance 时间间隔字符串转换为毫秒。

    :param interval: Binance 时间间隔字符串。
    :return: 转换后的毫秒值。
    """
    seconds_per_unit: Dict[str, int] = {
        "s": 1,
        "m": 60,
        "h": 60 * 60,
        "d": 24 * 60 * 60,
        "w": 7 * 24 * 60 * 60,
    }
    try:
        return int(interval[:-1]) * seconds_per_unit[interval[-1]] * 1000  # 计算毫秒
    except (ValueError, KeyError):
        return None  # 如果解析失败，返回 None


def round_step_size(quantity: Union[float, Decimal], step_size: Union[float, Decimal]) -> float:
    """将给定数量四舍五入到特定的步长。

    :param quantity: 需要四舍五入的数量。
    :param step_size: 步长。
    :return: 四舍五入后的数量。
    """
    quantity = Decimal(str(quantity))  # 转换为 Decimal 类型
    return float(quantity - quantity % Decimal(str(step_size)))  # 四舍五入


def convert_ts_str(ts_str):
    """将时间戳字符串转换为毫秒时间戳。

    :param ts_str: 时间戳字符串或整数。
    :return: 转换后的时间戳。
    """
    if ts_str is None:
        return ts_str
    if type(ts_str) == int:
        return ts_str
    return date_to_milliseconds(ts_str)  # 转换为毫秒


def get_loop():
    """检查当前线程是否有事件循环，如果没有则创建一个新的事件循环。

    :return: 当前线程的事件循环。
    """
    try:
        loop = asyncio.get_event_loop()  # 获取当前事件循环
        return loop
    except RuntimeError as e:
        if str(e).startswith("There is no current event loop in thread"):
            loop = asyncio.new_event_loop()  # 创建新的事件循环
            asyncio.set_event_loop(loop)  # 设置为当前事件循环
            return loop
        else:
            raise  # 其他异常抛出