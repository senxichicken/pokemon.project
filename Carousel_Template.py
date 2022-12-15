from linebot.models import *
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)


def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='各道館資訊',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://drive.google.com/uc?export=view&id=1Rf5TILMDF-EdkRem2wFw9pQ82nuAnGm2',
                    title='草路鎮館主是 亞洛 !',
                    text='是草系寶可夢訓練家!',
                    actions=[
                        PostbackTemplateAction(
                            label='他有的寶可夢!',
                            text='亞洛有的寶可夢!'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://drive.google.com/uc?export=view&id=13P6Osxm-vy3yfMQpHbFtDZxN51RoCsd1',
                    title='水舟鎮館主是 露璃娜 !',
                    text='是水系寶可夢訓練家!',
                    actions=[
                        PostbackTemplateAction(
                            label='他有的寶可夢!',
                            text='露璃娜有的寶可夢!'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://drive.google.com/uc?export=view&id=1GiYW--KDfVHBj636Vx9GtS67ynqBKBdD',
                    title='機擎市館主是 卡蕪 !',
                    text='是火系寶可夢訓練家!',
                    actions=[
                        PostbackTemplateAction(
                            label='他有的寶可夢!',
                            text='卡蕪有的寶可夢!'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://drive.google.com/uc?export=view&id=1ZWLe1djr3pShYX8rHUxh9dqAzyacqTQL',
                    title='溯傳鎮館主是 彩豆 !',
                    text='是只會出現在-劍版的格鬥系寶可夢訓練家!',
                    actions=[
                        PostbackTemplateAction(
                            label='他有的寶可夢!',
                            text='彩豆有的寶可夢!'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://drive.google.com/uc?export=view&id=1Ekxu4WYGN6anbArDu3AmxHY8c33Z5eMJ',
                    title='溯傳鎮館主是 歐尼奧 !',
                    text='是只會出現在-盾版的幽靈系寶可夢訓練家!',
                    actions=[
                        PostbackTemplateAction(
                            label='他有的寶可夢!',
                            text='歐尼奧有的寶可夢!'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://drive.google.com/uc?export=view&id=1dImWB2sRTKr89NXQ2hg0lPaU7mp_yuBL',
                    title='舞姿鎮館主是 波普菈 !',
                    text='是妖精系寶可夢訓練家!',
                    actions=[
                        PostbackTemplateAction(
                            label='他有的寶可夢!',
                            text='波普菈有的寶可夢!'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://drive.google.com/uc?export=view&id=1PHP8TIUu5Iyk3u5w4xUlQlaIO7NRb0Hd',
                    title='戰競鎮館主是 瑪瓜 !',
                    text='是只會出現在-劍版的岩石系寶可夢訓練家!',
                    actions=[
                        PostbackTemplateAction(
                            label='他有的寶可夢!',
                            text='瑪瓜有的寶可夢!'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://drive.google.com/uc?export=view&id=1lMv_S79wcJ3ktYDCPFlbCYs1gzgSPg_M',
                    title='戰競鎮館主是 美蓉 !',
                    text='是只會出現在-盾版的冰系寶可夢訓練家!',
                    actions=[
                        PostbackTemplateAction(
                            label='他有的寶可夢!',
                            text='美蓉有的寶可夢!'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://drive.google.com/uc?export=view&id=1cSKFOx_KA2CwCAWc6GaMOMBtZEe6Vv8S',
                    title='尖釘鎮館主是 聶梓 !',
                    text='是惡系寶可夢訓練家!',
                    actions=[
                        PostbackTemplateAction(
                            label='他有的寶可夢!',
                            text='聶梓有的寶可夢!'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://drive.google.com/uc?export=view&id=1y94fe_ce9Geh53RCuumkezCwoXzKt8ks',
                    title='拳關市館主是 奇巴納 !',
                    text='擁有岩石、地面與龍系的寶可夢訓練家!',
                    actions=[
                        PostbackTemplateAction(
                            label='他有的寶可夢!',
                            text='奇巴納有的寶可夢!'
                        )
                    ]
                ),
            ]
        )
    )
    return message
