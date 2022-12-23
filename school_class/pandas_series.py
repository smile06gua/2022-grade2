import pandas as pd

data = pd.Series([5, 4, -2, 3, 7], index = ["a","b","c","d","e"]) #索引
'''
print(data)
print("型態",data.dtype)
print("數量",data.size)
print("索引",data.index)

'''
#取得資料:根據順序、根據索引
print(data[2],data[0])
print(data["e"],data['d'])

#數字運算:基本、統計、順序
print(data.max())
print(data.sum())
print(data.prod())
print(data.std())
print(data.mean())
print(data.median())
print(data.nlargest(3))
print(data.nsmallest(3))

#字串運算:基本、串接、搜尋、取代
data = pd.Series(["Hello","smile","GOOD"])
print(data.str.lower())
print(data.str.upper())
print(data.str.len())
print(data.str.cat(sep =","))
print(data.str.contains("e"))
print(data.str.replace("Hello","Bye"))