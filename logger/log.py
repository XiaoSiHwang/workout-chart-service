import os
import logging
from logging.handlers import TimedRotatingFileHandler


# 定义文件夹路径
folder_path = 'log'

# 判断文件夹是否存在
if not os.path.exists(folder_path):
    # 如果文件夹不存在，创建文件夹
    os.makedirs(folder_path)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()

file_name = 'log/workout-chart-service.log'
fh = logging.FileHandler(filename=file_name)
formatter = logging.Formatter(
    "%(asctime)s - %(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s"
)
file_handler = TimedRotatingFileHandler(filename=file_name, when='D', interval=1, backupCount=2,
                                        encoding='utf-8')

if not logger.handlers:
  logger.addHandler(file_handler)
# 设置日志格式
file_handler.setFormatter(formatter)
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch) #将日志输出至屏幕
logger.addHandler(fh) #将日志输出至文件

