import urllib.request as req
import bs4 
#抓取PTT的網頁原始碼
def getData(url): 
    #建立request物件使不被網頁禁止
    request=req.Request(url, headers={
        "cookie":"over18=1",
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

    #抓取上一頁網址        
    nextLink = root.find("a", string ="‹ 上頁") #找到內文是‹ 上頁的a標籤
    return nextLink["href"]
#抓取一個頁面的函式
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
pages = int(input("需要抓取幾頁？ "))
while count<pages:
    pageURL ="https://www.ptt.cc"+ getData(pageURL)
    count+=1
