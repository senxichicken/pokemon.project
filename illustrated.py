import pandas as pd
from pokemon_linebot import *

pd.set_option("display.max_column", None)
pd.set_option("display.max_row", None)


def TVsearch(mtext):

    table = pd.read_html(
        "https://wiki.52poke.com/zh-hant/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89")
    t1 = table[2]


    df = pd.DataFrame(t1)
    df.columns = ["編號", "圖案", "中文", "日文", "英文", "本系", "副系", "0"]
    #print(df.columns)
    df2 = (df[df['中文'] == mtext])
    # print(df2['編號'])


    return df2
##----------以下是不聰明版-----------------###
# print(df["中文"][186]) #找到中文欄位內 最後一隻寶可夢的名字
# print(df.iloc[186][編號、圖案、中文、日文、英文、本系、副系])第186位精靈的表格
#mtext = '夢幻'

# for i in range(187):
# if df["中文"][i] == mtext:
# print(df.iloc[i])
