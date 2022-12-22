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
                    "text": "要查詢什麼呢!",
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
                        "label": "寶可夢",
                        "text": "寶可夢"
                    }
                },
                {
                    "type": "button",
                    "action": {
                        "type": "uri",
                        "label": "道具",
                        "uri": "https://wiki.52poke.com/wiki/%E9%81%93%E5%85%B7%E5%88%97%E8%A1%A8"
                    }
                },
                {
                    "type": "button",
                    "action": {
                        "type": "uri",
                        "label": "招式",
                        "uri": "https://wiki.52poke.com/wiki/%E6%8B%9B%E5%BC%8F%E5%88%97%E8%A1%A8"
                    }
                }

            ]
        }

    }
    message = FlexSendMessage(alt_text='圖鑑', contents=content)
    return message
