from flask import Flask
from automa import automa_bp
import logging
from logging.handlers import RotatingFileHandler
import os

# 配置日志
def setup_logger():
    # 创建日志目录（如果不存在）
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 创建日志格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # 配置文件处理器（使用 RotatingFileHandler 来控制日志文件大小）
    file_handler = RotatingFileHandler(
        'logs/app.log', 
        maxBytes=1024 * 1024,  # 1MB
        backupCount=10
    )
    file_handler.setFormatter(formatter)
    
    # 配置控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # 获取 Flask logger
    logger = logging.getLogger('flask.app')
    logger.setLevel(logging.INFO)
    
    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

app = Flask(__name__)
app.register_blueprint(automa_bp, url_prefix='/automa')

# 设置日志
logger = setup_logger()

@app.route('/')
def hello():
    logger.info('访问了首页')
    return "Hello, World!"

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
    logger.info(f'Flask app 启动成功 (Debug 模式: {debug_mode})')