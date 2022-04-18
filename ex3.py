fruitList = ["apple", "orange", "pear", "banana", "strawberry"]
fruitList.sort()

for fruit in fruitList:
    print(fruit, len(fruit))

fruitList.append("blue")
fruitList.append("red")
fruitList.append("yellow")

fruitList.reverse()
print(fruitList)