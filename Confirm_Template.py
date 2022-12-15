from linebot.models import *
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)


def Confirm_Template():
    message = TemplateSendMessage(
        alt_text='圖鑑',
        template=ConfirmTemplate(
            title = '要用什麼方式查詢呢?',
            text="要用什麼方式查詢呢?",
            actions=[
                PostbackTemplateAction(
                    label="文字或說話",
                    text='文字或說話',
                ),
                MessageTemplateAction(
                    label="上傳圖片",
                    text='上傳圖片',
                )
            ]
        )
    )
    return message
