# 导入所需的库
from flask import Flask, request
from moralis import evm_api
from dotenv import load_dotenv
import execute
import datetime
import locale
import os
import json

# 加载环境变量
load_dotenv()

# 从环境变量中获取Moralis API密钥
api_key = os.getenv("MORALIS_API_KEY")

# 设置本地化设置为美国英语
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

# 创建Flask应用实例
app = Flask(__name__)

# 定义获取价格的路由
@app.route("/getPrice", methods=["GET"])
def prices():
    # 从请求参数中获取地址和链信息
    address = request.args.get("address")
    chain = request.args.get("chain")
    
    # 设置请求参数
    params = {
        "chain": chain,
        "exchange": "pancakeswap-v2",
        "address": address,
    }

    # 使用Moralis API获取代币价格
    result = evm_api.token.get_token_price(
        api_key=api_key,
        params=params,
    )

    # 返回结果
    return result

# 定义webhook路由
@app.route("/webhook", methods=["POST"])
def webhook():
    # 解码接收到的webhook数据
    webhook = request.data.decode("utf-8")
    json_object = json.loads(webhook)

    # 获取交易列表
    txs = json_object["txs"]
    for tx in txs:
        # 获取交易的发送和接收地址
        from_address = tx["fromAddress"]
        to_address = tx["toAddress"]

        # 定义要监控的"鲸鱼"地址
        whale = "Your whale"
        whale = whale.lower()
        
        # 检查交易是否与"鲸鱼"地址相关
        if from_address == whale:
            print("sell")
            # 执行卖出分析和交易
            execute.execute_analysis_and_trade("sell")
        elif to_address == whale:
            print("buy")
            # 执行买入分析和交易
            execute.execute_analysis_and_trade("buy")
        else:
            print("no whale")

    # 返回成功响应
    return "ok"

# 主程序入口
if __name__ == "__main__":
    # 运行Flask应用，设置端口为5002，开启调试模式
    app.run(port=5002, debug=True)
