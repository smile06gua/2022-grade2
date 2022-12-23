import urllib.request as req
import bs4 
#抓取PTT的網頁原始碼

url = "https://www.ptt.cc/bbs/IU/index.html"
#建立request物件使不被網頁禁止
request=req.Request(url, headers={
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
})
#使用request物件開啟網址
with req.urlopen(request) as response:
    data = response.read().decode("utf-8") #轉換中文亂碼

#解析原始碼，取得標題
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_= "title") #尋找class="title"的 div標籤
for title in titles:
    if title.a != None: #有</a>標籤的才印出
        print(title.a.string ) #抓div下的標籤，再抓內容
#print(root.title.string) #抓到網頁的標籤，在抓內容字串