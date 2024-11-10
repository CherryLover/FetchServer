from flask import Blueprint, request, jsonify
import logging
import json

logger = logging.getLogger('flask.app')
automa_bp = Blueprint('automa', __name__)

@automa_bp.route('/')
def automa_index():
    logger.info('访问了 automa 首页')
    return "Welcome to Automa!"

@automa_bp.route('/submit_amazon_comment', methods=['POST'])
def submit_amazon_comment():
    try:
        # 获取请求中的 JSON 数据
        data = request.get_json()
        logger.info(f'提交 amazon comment 的数据为: {json.dumps(data)}')
        
        # 这里可以添加处理逻辑
        # TODO: 处理评论提交逻辑
        
        return jsonify({
            "status": "success",
            "message": "评论提交成功",
            "data": data
        }), 200
        
    except Exception as e:
        logger.error(f'提交 amazon comment 时发生错误: {str(e)}')
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

@automa_bp.route('/get_amazon_comment_url', methods=['GET'])
def get_amazon_comment_url():
    # 示例数据，实际应该从数据库或其他数据源获取
    urls = [
        "https://amazon.com/product1/comment",
        "https://amazon.com/product2/comment",
        "https://amazon.com/product3/comment"
    ]
    logger.info(f'需要爬取的 amazon comment URL: {urls}')
    return jsonify(urls), 200 