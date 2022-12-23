#AJAX是採用JavaScript程式技術
import urllib.request as req

#抓取PTT的網頁原始碼

url = "https://www.kkday.com/zh-tw/product/ajax_productlist/?keyword=新竹市&cat=TAG_4_4&sort=rdesc"
#建立request物件使不被網頁禁止
request=req.Request(url, headers={
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
})
#使用request物件開啟網址
with req.urlopen(request) as response:
    data = response.read().decode("utf-8") #轉換中文亂碼

import json
data = json.loads(data)
print(data)