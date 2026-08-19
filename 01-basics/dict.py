person = {"name" : "Ashwini D", "age": 28, "email": "ad@gmail.com"}
print(person["name"])
print(person["age"])
person["email"] = "am@gmail.com"
print(person["email"])
print(person.get("phone", "123"))
print("-----------------------------")
for key, value in person.items():
    print(key, value)
print("-----------------------------")
square_dict = {x : x**2 for x in range(10)}
for value in square_dict.items():
    print(value)

print("-----------------------------")

#Dictionary basics: Create a dictionary representing a "product" (name, price, quantity). 
# Print a sentence combining all three. Add a new key "in_stock" (boolean).
#  Use .get() to safely check for a key that doesn't exist, with a default value.
# Word frequency counter: Given a sentence like "the quick brown fox jumps over the lazy dog the fox runs", 
# split it into words (.split()) 
# and count how many times each word appears, 
# storing results in a dictionary. (Hint: loop through words, use .get(word, 0) + 1 pattern.)



product = {"name": "Computer", "price": 25000, "quantity" : 10}
print("Your order has beem placed successfully for a " + product["name"] + ", price per quantity is " + str(product["price"]) + " and the quantity is " + str(product["quantity"]))

product["in_stock"] = True

print(product)

print(product.get("name", 123))

sentence = "the quick brown fox jumps over the lazy dog the fox runs"
dict = {}
sentence = sentence.split()
print(sentence)
for word in sentence:
    if word in dict:
          dict[word] += 1
    else:
        dict[word] = 1
print(dict)


#.get(word, 0) + 1

dict2 = {}
for word in sentence:
    dict2[word] = dict2.get(word, 0)+1

print(dict2)


print ("-----------------------------------")


#List of dicts (this is the big one for DE work): 
# Create a list of 5 dictionaries, each representing an employee: {"name": ..., "department": ..., "salary": ...}. 
# Then:

employee = [
    {"name": "Ashwini",
     "department" : "ENTC",
     "salary": 900000
     },

    {
        "name": "Prachi",
        "department" : "ENTC",
        "salary": 500000
    },
     {
            "name": "Trupti",
            "department" : "ENTC",
            "salary": 500000
    },

     {
         "name" : "Pravin",
         "department" : "MECH",
         "salary" : 600000
     },
     {
         "name" : "Aditi",
         "department" : "Commerce",
         "salary" : 800000
     }
]

print(employee)


#Print names of everyone in the "ENTC" department
for emp in employee:
    if emp["department"] == "ENTC":
        print(f"{emp["name"]}")

#Calculate the total salary across all employees
sum = 0
for emp in employee:
    sum += emp["salary"]
print(sum)


#Find the employee with the highest salary
highest_salary = 0
highest_name = ""

for emp in employee:
    if emp["salary"] > highest_salary:
        highest_salary = emp["salary"]
        highest_name = emp["name"]

print(f"{highest_name} has the highest salary: {highest_salary}")