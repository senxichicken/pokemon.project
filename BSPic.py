import requests                                                             #用來對網站發出請求的套件                                                               #用來處理資料夾的套件
import bs4  
import re


def BSpic(num,eng):
    #print(num)
    url = "https://wiki.52poke.com/wiki/File:"+num+eng+".png"
    #print(url)
    request = requests.get(url)
    data = bs4.BeautifulSoup(request.text, "lxml")   
    imageData = data.find_all('img',{"alt":"File:"+num+eng+".png"},limit = 1)
    


    PKUrl = []        
    #print(imageData)
    PKUrl.append(imageData[0].attrs['src'])                                                        
    PKUrl = re.sub("\[|\]","",str(PKUrl))
    #print(PKUrl)

    return PKUrl

    
#abc = BSpic("#1008","Miraidon")
