import logging.handlers, os


def log_conf():
    """初始化日志配置"""
    # 日志文件位置
    logpath = "./log"
    # 日志器
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 处理器 -控制台
    sh = logging.StreamHandler()
    # 处理器 - 文件
    trfh = logging.handlers.TimedRotatingFileHandler(filename=logpath + os.sep + "mini.log", when="midnight",
                                                     interval=1,
                                                     backupCount=7,
                                                     encoding="utf-8")

    # 创建格式化器
    f = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(f)
    # 把格式化器添加到处理器中
    sh.setFormatter(formatter)
    trfh.setFormatter(formatter)
    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(trfh)


# 请求通用url
base_url = "http://e.cn/api/v1"

# 微信code
code = "033KhKkl2bwSM54mZTll2ODdnl2KhKk0"

# 请求头
headers = {
    "Content-Type": "application/json",
    "token": "da1b59cdf16c4bcc1f5a0a4c13dcf4b8"
}
