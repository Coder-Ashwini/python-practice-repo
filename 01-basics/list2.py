#List basics: Create a list of 5 favorite movies. Print the first, last, and a slice of the middle 3. Add a new movie, remove one, then print the sorted list.

movies = ["ZNMD", "YJHD", "K3G", "DDLJ", "Piku"]
print(movies[0])
print ("-------------------------")
print(movies[-1])
print ("-------------------------")
print(movies[1:4])
print ("-------------------------")
movies.append("OMG")
print ("-------------------------")
movies.remove("DDLJ")
print ("-------------------------")
movies.sort()

for movie in  movies:
    print(movie)


#List comprehension: Given numbers = [3, 8, 15, 22, 9, 41, 6], create a new list containing only the even numbers using a list comprehension.

numbers = [3, 8, 15, 22, 9, 41, 6]

even = [ x for x in numbers  if x%2 ==0]
print(even)