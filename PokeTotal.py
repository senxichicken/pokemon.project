from linebot.models import *
import BSPic
import illustrated
import re


def url(AtrOr, AtrSec):

    bug = 'https://drive.google.com/uc?export=view&id=1d6rqHZg86WiiYjiVpeAv5_vTSD_HyD_2'
    dark = 'https://drive.google.com/uc?export=view&id=15K0Xyp6f4pLBS3_sa7ggSSxuDmRglJ_K'
    dragon = 'https://drive.google.com/uc?export=view&id=1m7Zv_WuSiV2EHDpZvs7hO7cCzZdHQcKE'
    electric = 'https://drive.google.com/uc?export=view&id=1KUvw1Hax_9CdPXiaZi10NUq9UzRdfqI5'
    fairy = 'https://drive.google.com/uc?export=view&id=1BUhYqEmqQzJhn2ChE7PgdTMJ9giopgt6'
    fighting = 'https://drive.google.com/uc?export=view&id=1QLnmWwHpKfKLo_9dIGL4esVgR8C4voY6'
    flying = 'https://drive.google.com/uc?export=view&id=16KOQfBDqDOIugwlI904KDYI50PL1_xuV'
    grass = 'https://drive.google.com/uc?export=view&id=1OYG9CjnzFdz96UDS5ZtFrFgpi_xIL-6L'
    ghost = 'https://drive.google.com/uc?export=view&id=1euso5UoRiKvapuDgtly_8VFNGzaYEuni'
    fire = 'https://drive.google.com/uc?export=view&id=1iqHcJrLTcrAxx3pofj5od3Mi5estppWB'
    ground = 'https://drive.google.com/uc?export=view&id=1psUkVO3c5yDUuEHK8hXuhunJQPNgLgms'
    normal = 'https://drive.google.com/uc?export=view&id=1RufdYNoVip9gBzP2T_90OGvfgud6vOSP'
    ice = 'https://drive.google.com/uc?export=view&id=1aWKeTeA0JAO3v0l5bY1maYqG8T8sO6JY'
    poison = 'https://drive.google.com/uc?export=view&id=17waz1Od21FR3UeUa77B0yQBkh-0XvoYN'
    steel = 'https://drive.google.com/uc?export=view&id=1XtHGnlFCWI9-8cG9g3tq1I-A-bHvWcMI'
    psychic = 'https://drive.google.com/uc?export=view&id=1z1m0QR88GJXpMBOoZ1GTt4b0qI_0bqsn'
    water = 'https://drive.google.com/uc?export=view&id=1GnkOYdN24E6PCGhFCkwMeyVvv36NpN7v'
    rock = 'https://drive.google.com/uc?export=view&id=1pmFLJQyiP9gmmbTq7oouVkTRg44hNXKB'
    AtrOriUrl = ''
    AtrSecUrl = ''
    EngUrl = [bug, dark, dragon, electric, fairy, fighting, flying, grass,
              ghost, fire, ground, normal, ice, poison, steel, psychic, water, rock]
    ChEng = ["蟲", "惡", "龍", "電", "妖精", "格鬥", "飛行", "草", "幽靈",
             "火", "地面", "一般", "冰", "毒", "鋼", "超能力", "水", "岩石"]
    #print(AtrOr,AtrSec)
    for i in range(0,17):
        if AtrOr == ChEng[i]:
            AtrOriUrl = EngUrl[i]
        #print("che=="ChEng[i])   
        if AtrSec == ChEng[i]:
            AtrSecUrl = EngUrl[i]
        #print("che=="ChEng[i])
        #print("Ori="+AtrOriUrl, "Sec="+AtrSecUrl)
    return AtrOriUrl, AtrSecUrl

def Poke_Total(PokeUrl, Ch, Jp, Eng, Area, AtrOr, AtrSec, AtrOriUrl, AtrSecUrl):
    PokeUrl = re.sub("\'","",PokeUrl)
    PokeUrl = PokeUrl[18:]
    
    PokeUrl = 'https://s1.52poke.wiki'+PokeUrl
    a = Area
    Area = AtrSec
    AtrSec = a
    #print(PokeUrl)
    content = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": PokeUrl,
            "size": "full",
            "aspectRatio": "20:13"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "image",
                    "url": AtrOriUrl
                },
                {
                    "type": "image",
                    "url": AtrSecUrl
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": []
                },
                {
                    "type": "text",
                    "text": Ch,
                    "align": "center",
                    "size": "xl"
                },
                {
                    "type": "text",
                    "text": "日文:"+Jp+"    英文:"+Eng,
                },
                {
                    "type": "text",
                    "text": "本系:"+AtrOr+"    副系:"+AtrSec
                },
                {
                    "type": "text",
                    "text": "是"+Area+"的寶可夢!",
                    "style": "italic"
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "uri",
                        "label": "點我查看更多!",
                        "uri": "https://wiki.52poke.com/wiki/"+Eng
                }
                }
            ]
        }
    }
    message = FlexSendMessage(alt_text='道館館主', contents=content)
    return message
