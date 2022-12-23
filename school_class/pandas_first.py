import pandas as pd

#建立Series
data = pd.Series([20,10,15])

print(data)
print(data.max()) #最大值
print(data.median()) #中位數

data = data*2
print(data)

data = data == 20 
print(data)



#建立 DataFrame
data = pd.DataFrame({
    "name":["Amy","Jimmy","Bob"],
    "salary":[30000, 40000,20000]
})
print(data)
print(data["name"]) #取得特定欄位
print(data.iloc[0]) #取得特定列