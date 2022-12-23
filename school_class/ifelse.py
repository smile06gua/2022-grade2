#BMI
print("#BMI")
height = int(input("身高:"))
weight = int(input("體重:"))
BMI = weight/((height/100)*(height/100))
print(BMI)
if BMI >= 28.5:
    print("肥胖")
elif BMI >= 24:
    print("超重")
elif BMI >= 18.5:
    print("標準")
else:
    print("過輕")
print("====================")

