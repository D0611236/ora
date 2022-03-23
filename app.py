from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import random



app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('yivMuXMVVCYp4akbbyWixSoZpjCquczpnjw1PMsd63aGDPAoGVAmtBNpiKX1RvTu9NLh6g1OAGwJ/ploFtg4hPKNbBCtJS+Q52jD6KdbZBWM1uerozP0J2PPGdGzcI0d92kaHHYT1hHLmSjgGkCnfQdB04t89/1O/w1cDnyilFU=')
#or line_bot_api = 'Channel_token'

# Channel Secret
handler = WebhookHandler('b1874a7a204e95099e021932f7da6f0f')
#or handler = 'Channel_secret'

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get = event.message.text
#event.gessage.text接收使用者文字訊息
    
    message = TextSendMessage(text = get)


    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run()
