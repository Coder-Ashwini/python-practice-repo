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

emp_dep = {}

for emp in employee:
    dept = emp["department"]
    name = emp["name"]
    if dept not in emp_dep:
        emp_dep[dept] = [name] 
    else:
        emp_dep[dept].append(name)

print(emp_dep)

 #   print(dep)

#  Given {"Alex": 85, "Sam": 92, "Jo": 76}, find the student with the highest score without using max() — loop over .items() and track the best as you go.
def highest_score(dict):
    best_name = None
    best_score = float('-inf')
    for value in dict.values():
        if value > best_score:
            best_score = value
            best_name = name
    return best_name,best_score


dict = {"Alex": 85, "Sam": 92, "Jo": 76}
print(highest_score(dict))

# Merge d1 = {"a": 10, "b": 20} and d2 = {"b": 5, "c": 30} — if a key exists in both, add the values ("b" → 25).
def merge_dict(d1, d2):
    for key in d2:
        if key in d1:
            d1[key] = (d1[key] + d2[key])
        else:
            d1[key] = d2[key]
    return d1

d1 = {"a": 10, "b": 20} 
d2 = {"b": 5, "c": 30, "d" :40} 
print(merge_dict(d1,d2))

# Given ["cat", "elephant", "dog"], build {"cat": 3, "elephant": 8, "dog": 3} — word to its length.
def word_len(lst):
    result = {}
    for word in lst:
        result[word] = len(word)
    return result

lst = ["cat", "elephant", "dog"]
print(word_len(lst))

# Invert {"a": 1, "b": 2} → {1: "a", 2: "b"}. 
def invert_dict(dict):
    result_dict = {}
    for key, value in dict.items():
        result_dict[value] = key
    return result_dict

dict = {"a": 1, "b": 2, "c" : 1}

print(invert_dict(dict))

# Think first: what happens with duplicate values?: The previous value will get replaced by the later value.

# Given a dict of dicts (nested), like:
# python
# employees = {
#     "e1": {"name": "Alex", "age": 30},
#     "e2": {"name": "Sam", "age": 25}
# }
# Loop through and print each employee's name and age on one line, e.g. "Alex is 30 years old".

def nested_dict(employees):
    for emp_id, details in employees.items():
        print(f"{details['name']} is {details['age']} years old")

employees = {
    "e1": {"name": "Alex", "age": 30},
    "e2": {"name": "Sam", "age": 25}
}
nested_dict(employees)

# Write a function safe_get(d, key) that returns the value for key if it exists, or "Not Found" if it doesn't — without using .get() 
#     (use in and if/else instead, 
#     to make sure you understand what .get() is doing under the hood).

def safe_get(d, key):
    if key in d:
        return d[key]
    else:
        return "Not Found"

d = {"b": 5, "c": 30, "d" :40} 
print(safe_get(d, 'c'))

# Grouping & aggregating (the DE bread and butter)
# Given a list of transaction dicts:
# python
# transactions = [
#     {"user": "Alex", "amount": 100, "category": "food"},
#     {"user": "Sam", "amount": 50, "category": "travel"},
#     {"user": "Alex", "amount": 200, "category": "travel"},
#     {"user": "Sam", "amount": 75, "category": "food"},
#     {"user": "Alex", "amount": 30, "category": "food"},
# ]
# Calculate total spend per user → {"Alex": 330, "Sam": 125}.


transactions = [
    {"user": "Alex", "amount": 100, "category": "food"},
    {"user": "Sam", "amount": 50, "category": "travel"},
    {"user": "Alex", "amount": 200, "category": "travel"},
    {"user": "Sam", "amount": 75, "category": "food"},
    {"user": "Alex", "amount": 30, "category": "food"},
]

result = {}

for spend in transactions:
    name = spend['user']  
    # print(spend['amount'])
    if name in result:
        result[name] = result[name] + spend['amount']
    else:
        result[name] = spend['amount']
print(result)

# From the same data, calculate total spend per category → {"food": 205, "travel": 250}.

result2 = {}
for spend in transactions:
    item = spend['category']
    if item in result2:
        result2[item] = result2[item] + spend['amount']
    else:
        result2[item] = spend['amount']

print(result2)

# Two-level grouping: total spend per user, broken down by 
# category → {"Alex": {"food": 130, "travel": 200}, "Sam": {"travel": 50, "food": 75}}. 
# (Hint: you'll need a dict-of-dicts, and .setdefault() becomes genuinely useful here — or nested if key not in d.)





# Comparing & combining dicts
# 4. Given inventory = {"apples": 50, "bananas": 30, "oranges": 20} and sold = {"apples": 15, "bananas": 40, "grapes": 5}, calculate remaining stock after sales. What should happen for "grapes" (sold but never in inventory) and "oranges" (in inventory but never sold)? Decide and handle both cases.
# Given two dicts representing sets of skills, dev1 = {"python": 3, "sql": 2} and dev2 = {"python": 5, "java": 4}, find the skills common to both, and for common skills, keep the higher experience value.
# Sorting dicts (new territory)
# 6. Given scores = {"Alex": 85, "Sam": 92, "Jo": 76, "Mira": 92}, print students sorted by score, highest first. (Hint: look up sorted() with a key= argument — new concept, ask if you want it explained before trying.)
# From the same scores dict, return the top 2 students as a list of (name, score) tuples.
# Challenge — combines everything
# 8. Given the transactions list from #1, find the user who spent the most overall, and also return which category was their biggest spend within that. E.g. output might be ("Alex", 330, "travel") — Alex spent the most overall, and travel was his biggest single category.
# Try these in batches — #3 and #8 are the meaty ones. Let me know if sorted(..., key=...) in #6 needs an explainer before you dive in, or if you want to try it cold first.