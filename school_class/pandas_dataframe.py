import pandas as pd

data = pd.DataFrame({
    "name":["Amy","Jimmy","Bob"],
    "salary":[30000, 40000,20000]
},index=["a","b","c"]) #index建立索引

print(data)

print("型態",data.shape)
print("數量",data.size)
print("索引",data.index)


#取得列(橫向)資料:根據順序、根據索引 !變成單維

print("取得第二列",data.iloc[1],sep="\n")
print("取得第c列", data.loc["c"], sep = "\n")

#取得欄(直向)資料:根據欄位名稱 !變成單維
print("取得name欄位", data["name"], sep = "\n")


#單雙維應用
names=data["name"]#取得單維度資料
print("把name轉大寫",names.str.upper(), sep = "\n")

salaries = data["salary"]
print("薪水平均值",salaries.mean())


#建立新欄位
data["revenue"]= [500000, 400000, 300000]  # data[新欄位名稱] = list
data["ranks"] = pd.Series([3, 6, 1], index = ["a","b", "c"])
 # data[新欄位的名稱] = Series的資料
data["cp"] = data["revenue"]/data["salary"]
print(data)
