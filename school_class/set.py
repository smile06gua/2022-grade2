#集合 set
#建立集合

langs = {"python", "c", "Java"}
print(langs)
print(type(langs)) #資料類別

#不同資料組成
langs2 = {1, "python", (2, 5, 4)}
#langs2 = {1, "python", [2, 5, 4]}產生錯誤，可變元素不可當集合

#建立空集合
langs = {} #變為dict型態，這是建立字典
print(type(langs)) 
langs = set() #使用函數建立空集合，資料型態set
print(type(langs))

#string建立集合
langs = set("Hello Python! XDDD") #經過集合處理，集合內元素不重複
#list建立集合
friuts = ["banana", "orange", "grape","apple", "apple"]
langs = set(friuts) #langs = set(["banana", "orange", "grape","apple", "apple"]) 
print(langs) #元素不重複
#tuple建立集合
langs = set(("Hello","Py", "C", "Java", "C"))
print(langs) #不重複

#dict建立集合，鍵被當作元素
asia = {"Taiwan":"taipei", "Japan":"Tokyo"}
asiaSet = set(asia)

#交集 & (intersection)
math = {"May","Jimmy","Toby","Vivian"}
english = {"Jimmy", "Tommy", "Lisa","Vivian"}
both = math & english
print(both)

A = {"May","Jimmy","Toby","Vivian"}
B = {"Jimmy", "Tommy", "Lisa","Vivian"}
AB = A.intersection(B) #A和B的交集
BA = B.intersection(A) #B和A的交集

#聯集 | (union)
math = {"May","Jimmy","Toby","Vivian"}
english = {"Jimmy", "Tommy", "Lisa","Vivian"}
all = math | english
print(all)

A = {"May","Jimmy","Toby","Vivian"}
B = {"Jimmy", "Tommy", "Lisa","Vivian"}
AB = A.union(B) #A和B的聯集
BA = B.union(A) #B和A的聯集

#差集 - (difference)
math = {"May","Jimmy","Toby","Vivian"}
english = {"Jimmy", "Tommy", "Lisa","Vivian"}
mathOnly= math - english
print(mathOnly)
englishOnly = english - math
print(englishOnly)

A = {"May","Jimmy","Toby","Vivian"}
B = {"Jimmy", "Tommy", "Lisa","Vivian"}
AB = A.difference(B) #A和B的差集
BA = B.difference(A) #B和A的差集

#對稱差集 ^ (symmetric difference)
math = {"May","Jimmy","Toby","Vivian"}
english = {"Jimmy", "Tommy", "Lisa","Vivian"}
mathOnly_and_englishOnly = math ^ english
print(mathOnly_and_englishOnly)

A = {"May","Jimmy","Toby","Vivian"}
B = {"Jimmy", "Tommy", "Lisa","Vivian"}
AB = A.symmetric_difference(B) #A和B的對稱差集
BA = B.symmetric_difference(A) #B和A的對稱差集

#等於，不等於 == != 
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {1, 2, 3, 4, 5}
print("A集合和B集合相等", A == B)
print("A集合和C集合相等", A == C)
print("A集合和B集合不相等", A != B)
print("A集合和B集合不相等", A != C)

#在集合內 in 不在集合內 not in 回傳Bool
fruits = set("banana")
print("a屬於friuts集合", 'a' in friuts)
print("d屬於friuts集合", 'd' in friuts)
print("a不屬於friuts集合", 'a' not in friuts)
print("d不屬於friuts集合", 'd' not in friuts)
boolean = 'b' in fruits
print("b in fruits",boolean)
boolean = 'b' not in fruits
print("b not in fruits", boolean)

#適用集合的方法
#add()
names = {"Amy","Jimmy","Tony"}
names.add("Alice")
print(names)
names.add("Vivian")
print(names)
num = (1, 2, 3)
names.add(num)
print(names) #集合為無序，可能出現不同排列
#copy()
numset = {1, 2, 3}
deep_numset = numset
deep_numset.add(10)
print("賦值:", deep_numset)
shallow_numset = numset.copy()
shallow_numset.add(10)
print("淺拷貝:", shallow_numset)
#remove()
numset.remove(3)
print(numset)
#numset.remove(4) #刪除不存在元素，出現錯誤
print(numset)
#discard() 無論刪除解果回傳值為None
numset = {1, 2, 3, 4, 5}
numset.discard(1)
print(numset)
numset.discard(0) #刪除不存在元素，不出現錯誤
print(numset)
#pop() 隨機刪除
numset = {1, 2, 3, 4, 5}
new_numset = numset.pop() #回傳刪除的元素
print(numset)
print(new_numset) 
#clear() 刪除所有元素，回傳None
numset = {1, 2, 3, 4, 5}
numset.clear()
empty_set = set()
empty_set.clear()
print(numset)
print(empty_set)
#isdisjoint() 兩集合沒有共同元素回傳False 反之回傳True
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {8, 9, 0}
boolean = A.isdisjoint(B)
print(boolean)
boolean = A.isdisjoint(C)
print(boolean)
#issubset() 是否為另一個函式的子集合，是回傳True，否回傳False
A = {3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {8, 9, 0}
boolean = A.issubset(B)
print(boolean)
boolean = A.issubset(C)
print(boolean)
#issuperset() 是否為另一個函式的父集合
boolean = B.issubset(A)
print(boolean)
boolean = C.issubset(A)
print(boolean)
#intersection_update() 回傳交集
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {1, 2, 3, 4, 5}
A.intersection_update(B) #A B的交集
A.intersection_update(B,C) #A B C的交集
#update() #將另依函式加入當前函式
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
A.update(B)
print(A)
#difference_update() #刪除兩集合重複的元素
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
A.difference_update(B)
print(A)
print(B)
#symmetric_difference_update() #對稱差集
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
A.symmetric_difference_update(B)
print(A)
#凍結集合(frozenset)凍結後不可使用add(),remove()
A = frozenset([4, 5, 6])
B = frozenset([1, 5, 3])
print(A)
print(B)
print(A & B)
print(A | B)
X = A.intersection(B)
print(X)
