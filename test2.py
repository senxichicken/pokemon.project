import pandas as pd
from linebot import LineBotApi, WebhookHandler
from linebot.models import *
from linebot.exceptions import InvalidSignatureError
from pokemonnum import *
import BSPic
import re

pd.set_option("display.max_column", None)
pd.set_option("display.max_row", None)

table = pd.read_html(
    "https://wiki.52poke.com/zh-hant/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89")

df = pd.concat([table[2], table[3], table[4], table[5], table[6],
               table[7], table[8], table[9], table[10]], ignore_index=True)
df = pd.DataFrame(df).dropna(axis=1, how='any')
df.columns = ["編號",  "中文", "日文", "英文", "本系", "副系"]
df['中文'] = df['中文'].replace('*','')
print(df)
df1 = df[df['中文'] == '波克基斯' ]
df1 = df1.values.tolist()
df1 = df1[0]
#print(df1)
