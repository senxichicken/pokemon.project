import pandas as pd 
from linebot.models import *

def PokeNum(mtext,df):
    '''table = pd.read_html(
           "https://wiki.52poke.com/zh-hant/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89")

    df = pd.concat([table[2],table[3],table[4],table[5],table[6],table[7],table[8],table[9],table[10]],ignore_index=True)
    df = pd.DataFrame(df).dropna(axis = 1,how = 'any')

    df.columns = ["編號",  "中文", "日文", "英文", "本系", "副系"]'''
    # print(df.columns)
#print(type(len(df)))
#print(df)
#print(df[df['編號']== '#001'])
    df1 = (df[df['中文'] == mtext])
    dfn = df1['編號']
#print(df1)
#print(str(dfn).find("#"))
    pos = str(dfn).find("#") 
    dfn = int(str(df1['編號'])[pos+1 :].split("\n")[0])
#print(dfn)
    return dfn
