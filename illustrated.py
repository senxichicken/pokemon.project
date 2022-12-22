import pandas as pd
from linebot import LineBotApi, WebhookHandler
from linebot.models import *
from linebot.exceptions import InvalidSignatureError
from pokemonnum import * 
import BSPic

pd.set_option("display.max_column", None)
pd.set_option("display.max_row", None)


def TVsearch(mtext):
    table = pd.read_html(
            "https://wiki.52poke.com/zh-hant/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89")

    df = pd.concat([table[2],table[3],table[4],table[5],table[6],table[7],table[8],table[9],table[10]],ignore_index=True)
    df = pd.DataFrame(df).dropna(axis = 1,how = 'any')

    df.columns = ["編號",  "中文", "日文", "英文", "本系", "副系"]
    # print(df.columns)
    pkn = PokeNum(mtext,df) 
    df1 = df[df['中文'] == mtext ]
    df1 = df1.values.tolist()
    df1 = df1[0]

    if  pkn <= 151 and pkn > 0:
    #print(type(mtext))
    # print(df1['編號'])
    # print(type.df1[0])確認值是否為str
        num = df1[0]
        ch = df1[1]
        jp = df1[2]
        eng = df1[3]
        AtrOr = df1[4]
        AtrSec = df1[5]
        Area = "關都地區"
        BSPic.BSpic(num,eng)
        return num,ch,jp,eng,AtrOr,AtrSec,Area
    elif pkn > 151 and pkn <= 251:
        df1 = df[df['中文'] == mtext]
        df1 = df1.values.tolist()
        df1 = df1[0]
    # print(type.df1[0])確認值是否為str
        num = df1[0]
        ch = df1[1]
        jp = df1[2]
        eng = df1[3]
        AtrOr = df1[4]
        AtrSec = df1[5]
        Area = "城都地區"
        BSPic.BSpic(num,eng)
        return num,ch,jp,eng,AtrOr,AtrSec,Area
    elif pkn > 251 and pkn <= 386: 
        df1 = df[df['中文'] == mtext]
        df1 = df1.values.tolist()
        df1 = df1[0]
    # print(type.df1[0])確認值是否為str
        num = df1[0]
        ch = df1[1]
        jp = df1[2]
        eng = df1[3]
        AtrOr = df1[4]
        AtrSec = df1[5]
        Area = "豐緣地區"
        BSPic.BSpic(num,eng)
        return num,ch,jp,eng,AtrOr,AtrSec,Area
    elif pkn > 386 and pkn <= 493:
        df1 = df[df['中文'] == mtext]
        df1 = df1.values.tolist()
        df1 = df1[0]
    # print(type.df1[0])確認值是否為str
        num = df1[0]
        ch = df1[1]
        jp = df1[2]
        eng = df1[3]
        AtrOr = df1[4]
        AtrSec = df1[5]
        Area = "神奧地區"
        BSPic.BSpic(num,eng)
        return num,ch,jp,eng,AtrOr,AtrSec,Area
    elif pkn > 493 and pkn <= 649:
        df1 = df[df['中文'] == mtext]
        df1 = df1.values.tolist()
        df1 = df1[0]
    # print(type.df1[0])確認值是否為str
        num = df1[0]
        ch = df1[1]
        jp = df1[2]
        eng = df1[3]
        AtrOr = df1[4]
        AtrSec = df1[5]
        Area = "合眾地區"
        BSPic.BSpic(num,eng)
        return num,ch,jp,eng,AtrOr,AtrSec,Area
    elif pkn > 649 and pkn <= 721:
        df1 = df[df['中文'] == mtext]
        df1 = df1.values.tolist()
        df1 = df1[0]
    # print(type.df1[0])確認值是否為str
        num = df1[0]
        ch = df1[1]
        jp = df1[2]
        eng = df1[3]
        AtrOr = df1[4]
        AtrSec = df1[5]
        Area = "卡洛斯地區"
        BSPic.BSpic(num,eng)
        return num,ch,jp,eng,AtrOr,AtrSec,Area
    elif pkn > 721 and pkn <= 809:
        df1 = df[df['中文'] == mtext]
        df1 = df1.values.tolist()
        df1 = df1[0]
    # print(type.df1[0])確認值是否為str
        num = df1[0]
        ch = df1[1]
        jp = df1[2]
        eng = df1[3]
        AtrOr = df1[4]
        AtrSec = df1[5]
        Area = "阿羅拉地區"
        BSPic.BSpic(num,eng)
        return num,ch,jp,eng,AtrOr,AtrSec,Area
    elif pkn > 809 and pkn <= 905:
        df1 = df[df['中文'] == mtext]
        df1 = df1.values.tolist()
        df1 = df1[0]
    # print(type.df1[0])確認值是否為str
        num = df1[0]
        ch = df1[1]
        jp = df1[2]
        eng = df1[3]
        AtrOr = df1[4]
        AtrSec = df1[5]
        Area = "伽勒爾地區"
        BSPic.BSpic(num,eng)
        return num,ch,jp,eng,AtrOr,AtrSec,Area
    else:
        pkn > 905 and pkn <= 1008
        df1 = df[df['中文'] == mtext]
        df1 = df1.values.tolist()
        df1 = df1[0]
    # print(type.df1[0])確認值是否為str
        num = df1[0]
        ch = df1[1]
        jp = df1[2]
        eng = df1[3]
        AtrOr = df1[4]
        AtrSec = df1[5]
        Area = "帕底亞地區"
        BSPic.BSpic(num,eng)
        return num,ch,jp,eng,AtrOr,AtrSec,Area
        
        
    
'''if __name__ == '__main__':
    output = TVsearch("密勒頓")
    print(str(output[0])) #編號
    print(str(output[1])) #中文
    print(str(output[2])) #日文
    print(str(output[3])) #英文
    print(str(output[4]))
    print(str(output[5]))
    print(str(output[6]))'''
## ----------以下是不聰明版-----------------###
# print(df["中文"][186]) #找到中文欄位內 最後一隻寶可夢的名字
# print(df.iloc[186][編號、圖案、中文、日文、英文、本系、副系])第186位精靈的表格
#mtext = '夢幻'

# for i in range(187):
# if df["中文"][i] == mtext:
# print(df.iloc[i])
