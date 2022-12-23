import pandas as pd

print("========篩選練習1========")
data = pd.Series([30, 15, 20])
condition = [True, False, True]
filterdData = data[condition]
print(filterdData)
print()

print("========篩選練習2========")
data = pd.Series([30, 15, 20])
condition = data > 18
print(condition)
filterdData = data[condition]
print(filterdData)
print()

print("========篩選練習3========")
data = pd.Series(["您好", "Pandas","Python"])
condition = [True, False, True]
filterdData = data[condition]
print(filterdData)
print()

print("========篩選練習4========")
data = pd.Series(["您好", "Pandas","Python"])
condition = data.str.contains("P")
print(condition)
filterdData = data[condition]
print(filterdData)
print()

print("========篩選練習 DataFrame1========")
data = pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[30000, 50000, 40000]
})
print(data)
condition = [False, True, True]
filterdData = data[condition]
print(filterdData)
print()

print("========篩選練習 DataFrame2========")
data = pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[30000, 50000, 40000]
})
print(data)
condition = data["salary"]>=40000  #條件 ex. data["name"] == "Amy" 變成布林值列表
print(condition)
filterdData = data[condition]
print(filterdData)
print()