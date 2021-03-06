# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('xhJ6cjcGcttqpoKijQVKY8DBz0gkmojjN4PO+vvMSY2g9OC6EiuFLW8Zdg4yZlI8NcMCxEe33Wp/UK2iD5vLiLfAoPBnNyltG/imkMusB/Pkdq3jEGQOBr4IVLZvQTbdb6/njtt2uVHVpD24oBksfgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fc1d18cb66eb5ba288066cafb3881920')



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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

print('juhuhu')

if __name__ == '__main__':
    app.run(debug=True)


for i in range(0,10):
    print(i)