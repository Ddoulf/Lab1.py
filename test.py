# This is a simple Python script that iterates through a list of fruits and prints each fruit along with its position in the list. The position starts at 0 and increments by 1 for each fruit in the list.
fruits = ["apple", "banana", "orange", "grape", "kiwi"]

for position, fruit in enumerate(fruits): #what does enumerate do? it takes a list and returns the index and the value of each item in the list
    print(fruit, position)
i = 0
while i < len(fruits):          #what doesthis mean? it means while (i) is less than the length of the list fruits, do the following
    print(fruits[i])
    i = i + 1                   #what does this mean? it means increment (i) by 1 each time the loop runs


names = ["Alice", "Bob", "Charlie", "David", "Eve"]

for i in range(1, 11):          #what does this mean? it means for (i) in the range of 1 to 10, do the following
    print(i)
