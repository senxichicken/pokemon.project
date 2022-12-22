from linebot.models import *
import illustrated


def Carousel_template():
    content = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://drive.google.com/uc?export=view&id=1Rf5TILMDF-EdkRem2wFw9pQ82nuAnGm2",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "草路鎮館主是 亞洛 !",
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "text",
                            "text": "是草系寶可夢訓練家!",
                            "style": "italic"
                        }
                    ],
                    "maxHeight": "80px"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "他有的寶可夢!",
                            "align": "center",
                            "size": "xl"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "幼棉棉",
                                "text": "幼棉棉"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "白蓬蓬",
                                "text": "白蓬蓬"
                            }
                        },
                    ]
                }
            },
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://drive.google.com/uc?export=view&id=13P6Osxm-vy3yfMQpHbFtDZxN51RoCsd1",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "水舟鎮館主是 露璃娜 !",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "是水系寶可夢訓練家!",
                            "style": "italic"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "他有的寶可夢!",
                            "align": "center",
                            "size": "xl"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "角金魚",
                                "text": "角金魚"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "刺梭魚",
                                "text": "刺梭魚"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "暴噬龜",
                                "text": "暴噬龜"
                            }
                        },
                    ]
                }
            },
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://drive.google.com/uc?export=view&id=1GiYW--KDfVHBj636Vx9GtS67ynqBKBdD",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "機擎市館主是 卡蕪 !",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "是火系寶可夢訓練家!"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "他有的寶可夢!",
                            "align": "center",
                            "size": "xl"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "九尾",
                                "text": "九尾"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "風速狗",
                                "text": "風速狗"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "焚焰蚣",
                                "text": "焚焰蚣"
                            }
                        },
                    ]
                }
            },
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://drive.google.com/uc?export=view&id=1ZWLe1djr3pShYX8rHUxh9dqAzyacqTQL",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "溯傳鎮館主是 彩豆 !",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "是只會出現在-劍版的格鬥系寶可夢訓練家!"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "他有的寶可夢!",
                            "align": "center",
                            "size": "xl"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "戰舞郎",
                                "text": "戰舞郎"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "流氓熊貓",
                                "text": "流氓熊貓"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "蔥遊兵",
                                "text": "蔥遊兵"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "怪力",
                                "text": "怪力"
                            }
                        },
                    ]
                }
            },
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://drive.google.com/uc?export=view&id=1Ekxu4WYGN6anbArDu3AmxHY8c33Z5eMJ",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "溯傳鎮館主是 歐尼奧 !",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "是只會出現在-盾版的幽靈系寶可夢訓練家!"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "他有的寶可夢!",
                            "align": "center",
                            "size": "xl"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "哭哭面具",
                                "text": "哭哭面具"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "謎擬Q",
                                "text": "謎擬Q"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "魔靈珊瑚",
                                "text": "魔靈珊瑚"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "耿鬼",
                                "text": "耿鬼"
                            }
                        },
                    ]
                }
            },
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://drive.google.com/uc?export=view&id=1dImWB2sRTKr89NXQ2hg0lPaU7mp_yuBL",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "舞姿鎮館主是 波普菈 !",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "是妖精系寶可夢訓練家!"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "他有的寶可夢!",
                            "align": "center",
                            "size": "xl"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "雙彈瓦斯",
                                "text": " 雙彈瓦斯"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "大嘴娃",
                                "text": "大嘴娃"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "波克基斯",
                                "text": "波克基斯"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "霜奶仙",
                                "text": "霜奶仙"
                            }
                        },
                    ]
                }
            },
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://drive.google.com/uc?export=view&id=1PHP8TIUu5Iyk3u5w4xUlQlaIO7NRb0Hd",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "戰競鎮館主是 瑪瓜 !",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "是只會出現在-劍版的岩石系寶可夢訓練家!"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "他有的寶可夢!",
                            "align": "center",
                            "size": "xl"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "龜足巨鎧",
                                "text": " 龜足巨鎧"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "壺壺",
                                "text": "壺壺"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "巨石丁",
                                "text": "巨石丁"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "巨炭山",
                                "text": "巨炭山"
                            }
                        },
                    ]
                }
            },
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://drive.google.com/uc?export=view&id=1lMv_S79wcJ3ktYDCPFlbCYs1gzgSPg_M",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "戰競鎮館主是 美蓉 !",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "是只會出現在-盾版的冰系寶可夢訓練家!"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "他有的寶可夢!",
                            "align": "center",
                            "size": "xl"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "雪絨蛾",
                                "text": " 雪絨蛾"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "達摩狒狒",
                                "text": "達摩狒狒"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "冰砌鵝",
                                "text": "冰砌鵝"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "拉普拉斯",
                                "text": "拉普拉斯"
                            }
                        },
                    ]
                }
            },
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://drive.google.com/uc?export=view&id=1cSKFOx_KA2CwCAWc6GaMOMBtZEe6Vv8S",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "尖釘鎮館主是 聶梓 !",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "是惡系寶可夢訓練家!"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "他有的寶可夢!",
                            "align": "center",
                            "size": "xl"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "頭巾混混",
                                "text": " 頭巾混混"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "烏賊王",
                                "text": "烏賊王"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "堵攔熊",
                                "text": "堵攔熊"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "坦克臭鼬",
                                "text": "坦克臭鼬"
                            }
                        },
                    ]
                }
            },
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://drive.google.com/uc?export=view&id=1y94fe_ce9Geh53RCuumkezCwoXzKt8ks",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "拳關市館主是 奇巴納 !",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "擁有岩石、地面與龍系的寶可夢訓練家!"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "他有的寶可夢!",
                            "align": "center",
                            "size": "xl"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "龐岩怪",
                                "text": " 龐岩怪"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "沙漠蜻蜓",
                                "text": "沙漠蜻蜓"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "沙螺蟒",
                                "text": "沙螺蟒"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "鋁鋼龍",
                                "text": "鋁鋼龍"
                            }
                        },
                    ]
                }
            }
        ]
    }
    message = FlexSendMessage(alt_text='道館館主', contents=content)
    return message
