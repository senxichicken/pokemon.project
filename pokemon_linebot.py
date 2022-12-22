from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import *
from linebot.exceptions import InvalidSignatureError
import Confirm_Template
import Carousel_Template
import illustrated
import BSPic
import PokeTotal
import time
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

#boss = ["亞洛","露璃娜","卡蕪","彩豆","歐尼奧","波普菈","瑪瓜","美蓉","聶梓","奇巴納"] 

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    #print(type(mtext))

    if mtext == '圖鑑' :
        message = Confirm_Template.Confirm_template()
        line_bot_api.reply_message(event.reply_token, message)

###查詢方法###
    elif mtext == '文字或說話' :
        line_bot_api.reply_message(
            event.reply_token, TextMessage(text='請輸入或是說出您想查詢的寶可夢!'))
        '''while mtext == '文字或說話':
            message = TVsearch(mtext)
            line_bot_api.reply_message(event.reply_token,TextMessage(text = str(message[1])))'''
###--------###

#    elif mtext = '':

###單純的屬性相剋表###
    elif mtext == '屬性相剋表':
        picurl = 'https://drive.google.com/uc?export=view&id=1S0jgdZ_mTaabMTxcXrOkj9kSqUEQ_rJD'
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(
            original_content_url=picurl, preview_image_url=picurl))
###-----------###

    elif mtext == '各道館資訊':
        message = Carousel_Template.Carousel_template()
        line_bot_api.reply_message(event.reply_token, message)
   
    #elif illustrated.TVsearch(mtext) == True:
    elif mtext =='寶可夢': 
        line_bot_api.reply_message(
            event.reply_token, TextMessage(text='請輸入您要查詢的寶可夢!'))
    else:
        try:
            search(event,mtext)
        except:
            try:
                mtext = mtext+"*"
                search(event,mtext)
            except:
                line_bot_api.reply_message(
                event.reply_token, TextMessage(text='很抱歉沒有找到您查詢的寶可夢!'))

        
    #else:
        #line_bot_api.reply_message(
        #event.reply_token, TextMessage(text='抱歉!找不到您要查詢的寶可夢!'))
        
    
def search(event,mtext):
    num,ch,jp,eng,AtrOr,AtrSec,Area = illustrated.TVsearch(mtext)
    #print(num,ch,jp,eng,AtrOr,AtrSec,Area)
    PokeUrl = BSPic.BSpic(num,eng)
    AtrOriUrl, AtrSecUrl = PokeTotal.url(AtrOr,AtrSec)
    result = PokeTotal.Poke_Total(PokeUrl,ch,jp,eng,AtrOr,AtrSec,Area,AtrOriUrl, AtrSecUrl)
    #print(PokeUrl,ch,jp,eng,AtrOr,AtrSec,Area,AtrOriUrl, AtrSecUrl)
    line_bot_api.reply_message(event.reply_token,result)
    

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)

#定義屬性貼圖



if __name__ == '__main__':
    app.run()
