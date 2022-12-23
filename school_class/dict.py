# name_dict = {鍵:值}
fruits = {"banana":15, 'apple':20, 'watermelon':40}
print(fruits,type(fruits))
print(fruits['banana']) # name_dict['key']取得值
#建立空字典
none_dict = {}
print(none_dict)
#增加字典元素
fruits['grape'] = 30
print(fruits)
#更改元素
fruits['banana'] = 25
print(fruits)
#刪除特定鍵 del name_dict[key]
del fruits['grape']
print(fruits)
#pop()刪除特定元素並回傳所刪除元素
value = fruits.pop('watermelon')
print(fruits, value)
#name_dict.pop(key, default) 找不到key時回傳default設定的內容，若未設定則KeyError程式異常終止
value = fruits.pop('pear','does not exist') 
print(fruits, value)
#刪除所有元素
fruits.clear()
print(fruits)
#刪除字典 del name_dict
del fruits
#print(fruits) 錯誤!沒有定義fruits字典

#拷貝
fruits = {"banana":15, 'apple':20, 'watermelon':40}
new_fruits = fruits.copy()
print("ID =", id(fruits), fruits)
print("ID =", id(new_fruits), new_fruits)
#元素數量len()
print(len(fruits))
#驗證元素是否存在
print("watermelon in dict?", 'watermelon' in fruits)
print("grape in dict?", 'grape' in fruits)
#合併
fruits = {"banana":15, 'apple':20, 'watermelon':40}
fruits_second = {'grape':35}
fruits.update(fruits_second)
print(fruits)
#dict()處理雙值序列
nation = [['日本','東京'],['泰國','曼谷']]
nation_dict = dict(nation)
print(nation_dict)
#遍歷
fruits = {"banana":15, 'apple':20, 'watermelon':40}
for fruit_name, cost in fruits.items():
    print("\n水果:", fruit_name)
    print("價格::", cost)
for fruit_name in fruits.keys():
    print("\n水果:", fruit_name)
for fruit_name in fruits.values():
    print("\n價格::", cost)
#字典包字典
sports = {'Curry':{
    'sport':'basketball'},
          'Durant':{
    'sport':'baseball'}
}
print(sports)
#name_dict = dict.fromkeys(seq,value) 未設定value則以None為值
seq1 = ['name','city']
list_dict1 = dict.fromkeys(seq1)
print(list_dict1)
list_dict2 = dict.fromkeys(seq1, "Chicago")
print(list_dict2)
seq2 = ('name','city')
tup_dict1 = dict.fromkeys(seq2)
print(tup_dict1)
tup_dict2 = dict.fromkeys(seq2, "Chicago")
print(tup_dict2)
#get()
fruits = {"banana":15, 'apple':20, 'watermelon':40}
value = fruits.get('banana')
print(value)
value = fruits.get('orange') #不存在則回傳None
print(value)
#setdefault()
fruits = {"banana":15, 'apple':20, 'watermelon':40}
value = fruits.setdefault('banana')
print(fruits)
print(value)
value = fruits.setdefault('orange') #不存在則加入字典，未設定值則預設為None
print(fruits)
print(value)
value = fruits.setdefault('berry',100) #不存在則加入字典，值為100
print(fruits)
print(value)