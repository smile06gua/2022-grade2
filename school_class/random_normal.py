import random

#隨機選
"""
data=random.choice([1,2,4,6,10,20])
print(data)
"""

"""
data = random.sample([1,2,4,6,10,20],3)
print(data)
"""

#隨機換順序
"""
data=[1,5,8,20]
random.shuffle(data)
print(data)
"""

#隨機取亂數
"""
data=random.random()
print(data)
"""

#可指定範圍
"""
data=random.uniform(10, 100)
print(data)
"""

#取得常態分配亂數
"""
data=random.normalvariate(100,10) #(平均數,標準差)
print(data)
"""

