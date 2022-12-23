import pandas as pd

#讀取資料
data = pd.read_csv("googleplaystore.csv")#把csv格式的檔案讀取成一個DataFrame

#觀察
print("資料數量",data.shape)
print("資料欄位",data.columns)
print("_______________________")
#分析:評分的各種統計數據
'''
condition = data["Rating"] <= 5
data = data[condition]
print(data["Rating"])
print("平均數",data["Rating"].mean())
print("中位數",data["Rating"].median())
print("取得前一百個應用程式的平均",data["Rating"].nlargest(1000).mean())
'''

#分析:安裝數量的各種統計數據
#觀察
'''
print(data["Installs"][10472])#單獨觀察

data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]","").str.replace("Free",""))
print("平均數", data["Installs"].mean())
condition = data["Installs"]>100000
print("安裝數量大於100000的應用程式有幾個",data[condition].shape[0])
print("平均數",data["Installs"].mean())
'''

#基於資料的應用：關鍵字搜尋應用程式
keyword = input("請輸入關鍵字：")
condition = data["App"].str.contains(keyword, case = False) #不顧大小寫
print(data[condition]["App"])
print("包含關鍵字的應用程式數量：",data[condition].shape[0])
