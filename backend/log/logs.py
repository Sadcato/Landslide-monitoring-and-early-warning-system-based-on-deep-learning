import logging

# 配置日志记录器
def setup_logger():
    # 创建一个日志记录器
    logger = logging.getLogger("my_app_logger")
    logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG，记录所有级别的日志

    # 创建一个文件处理器，并设置级别为ERROR
    fh = logging.FileHandler("error.log")  # 日志文件名
    fh.setLevel(logging.ERROR)  # 只记录ERROR及以上级别的日志

    # 创建一个控制台处理器，用于记录DEBUG及以上级别的日志，方便调试
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # 创建日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给日志记录器添加处理器
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

# 初始化日志记录器
logger = setup_logger()

# 使用日志记录器记录错误
logger.error("This is an error message")