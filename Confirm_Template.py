from linebot.models import *
def Confirm_template():
    content = {
        "type": "bubble",
        "hero": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "要用什麼方式查詢呢?",
                    "size": "xl",
                    "weight": "bold",
                    "align": "center",
                    "margin": "xxl"
                }
            ],
            "alignItems": "center"
        },
        "footer": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "文字或說話",
                        "data": "文字或說話"
                    }
                },
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "上傳圖片",
                        "data": "上傳圖片"
                    }
                }
            ]
        }
    }
    message = FlexSendMessage(alt_text='圖鑑', contents=content)
    return message
