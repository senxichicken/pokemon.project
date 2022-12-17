from linebot.models import *


def Confirm_template():
    content = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "要用什麼方式查詢呢!",
                    "size": "xl",
                    "weight": "bold",
                    "align": "center"
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "文字或說話",
                        "text": "文字或說話"
                    }
                },
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "上傳圖片",
                        "text": "上傳圖片"
                    }
                }
            ]
        }
    }
    message = FlexSendMessage(alt_text='圖鑑', contents=content)
    return message
