from flask import Flask, request, jsonify
import os
import requests
import json

app = Flask(__name__)

print("🤖 飞书机器人启动成功！")

@app.route('/webhook', methods=['POST'])
def webhook():
    """处理飞书webhook"""
    try:
        data = request.json
        
        # 验证请求
        if 'challenge' in data:
            return jsonify({'challenge': data['challenge']})
        
        # 简单回复
        return jsonify({
            'msg_type': 'text',
            'content': json.dumps({
                'text': '🤖 飞书AI机器人已收到消息！\n发送"帮助"查看使用指南。'
            })
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>飞书机器人</title><meta charset="utf-8"></head>
    <body style="text-align:center;padding:50px;">
        <h1>🤖 飞书AI机器人</h1>
        <p style="color:green;">✅ 服务运行正常</p>
        <p>Webhook地址: /webhook</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
