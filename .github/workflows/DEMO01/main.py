import time
from execution.testnet_order_executor import TestnetOrderExecutor
from strategy.multi_strategy import MultiStrategy
from utils.logger import setup_logger

def main():
    # 设置日志记录器
    logger = setup_logger()
    
    # 初始化交易执行器
    order_executor = TestnetOrderExecutor()
    
    # 初始化多策略
    multi_strategy = MultiStrategy(order_executor)

    # 记录程序启动信息
    logger.info("Starting testnet trading bot with multiple strategies")

    try:
        # 执行所有策略
        multi_strategy.execute_strategies()
        logger.info("All strategies executed successfully")
    except Exception as e:
        logger.error(f"An error occurred while executing strategies: {e}")

if __name__ == "__main__":
    main()