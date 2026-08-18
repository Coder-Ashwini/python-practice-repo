fruits = ["Banana", "Apple", "Mango"]
fruits.append("Guava")
fruits.remove("Apple")
fruits.sort()
for fruit in fruits:
    print(fruit)

squares = [x*x for x in range(10)]
print(squares)

evens = [x for x in range(20) if x%2==0]
print(evens)