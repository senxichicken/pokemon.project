from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import *
from linebot.exceptions import InvalidSignatureError
from Confirm_Template import *
from Carousel_Template import *

app = Flask(__name__)


line_bot_api = LineBotApi(
    'k6eiUB3hH/29tSYqfLJc8g8WoSYA78H+8Uf7H3pLTxdawO8oh/8eeqvn8jKqEay9eZ90cgMcbEbOTCdmRv3IAfg8BymewgtbJxOHkFhyFf5VZeIF4Jc4p2mRMkHrS7u/xSH0YtTip8HX5Gjm69FKlgdB04t89/1O/w1cDnyilFU=')
# 使用者Channel access token'
handler = WebhookHandler('1f07dd59c38ef5064be5400b4bdce0df')
# 使用者Channel secret'


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-LINE-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
        return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
        mtext = event.message.text
        if mtext == '圖鑑':
            message = Confirm_template()
            line_bot_api.reply_message(event.reply_token, message)
        elif mtext == '屬性相剋表':
            picurl = 'https://drive.google.com/uc?export=view&id=1S0jgdZ_mTaabMTxcXrOkj9kSqUEQ_rJD'
            line_bot_api.reply_message(event.reply_token, ImageSendMessage(
                original_content_url=picurl, preview_image_url=picurl))

        elif mtext == '各道館資訊':
            message = Carousel_template()
            line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)








if __name__ == '__main__':
    app.run()
