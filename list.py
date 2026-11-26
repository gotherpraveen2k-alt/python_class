#list indexing question



#fruits = ["apple", "banana", "mango", "orange"]
#print(fruits[0])
#"apple"


#print(fruits[1])
#"banana"


#print(fruits[2])
#"mango"


#print(fruits[-1])
#"orange"

#numbers = [100, 200, 300, 400, 500]
#print(numbers[1])
#200


#print(numbers[-2])
#400

#print(numbers[-4])
#200

#print(numbers[4])
#500


#student = ["Rahul", 20, True, "Python"]
#print(student[0])
#"Rahul"

#print(student[-1])
#"Python"


#print(student[-2])
#True


#print(student[2])
#20

#a = ["India", "Japan", "USA", "France"]
#print(a[0][0])
#I


#print(a[0][2]) 
#d


# print(a[1][1])
#a

#print(a[-1][-1])
#e

#colors = ["red", "green", "blue"]
#print(colors[1][0])
#g

#print(colors[2][2])
#u

#print(colors[-1][0])
#b

#a = [ [10, 20, 30], [40, 50, 60], [70, 80, 90] ]
#print(a[0])
# [10, 20, 30]


#print(a[1])
#[40, 50, 60]

#print(a[2])
#[70, 80, 90]

#print(a[0][1])
#20

#print(a[1][2])
#60

#print(a[2][0])
#70

#students = [ ["Rahul", 20], ["Priya", 21], ["Amit", 19] ]
#print(students[0][0])
#"Rahul"


#print(students[1][1])
#21


#print(students[2][0])
#"Amit"


#data = [ 100, "Python", [10, 20, 30], True, ["India", "Japan", "USA"] ]
#print(data[1])
#"Python"


#print(data[2][0])
#10


#print(data[2][-1]) 
#30


#print(data[4][1])
#"Japan"

#print(data[4][-1])
#"USA"

#a = [ "Hello", [1, 2, 3], "India", [True, False, [100, 200, 300]] ]
#print(a[0][1]) 
#e

#print(a[1][2])
#3

#print(a[2][3])
#i

#print(a[3][2][1])
#200

#x = ["Python", [10, 20, 30], "India"]
#print(x[0][0])
#p

#print(x[0][-1])
#n

#print(x[1][1])
#20

#print(x[2][2])
#d

#x = [ [1, 2], [3, 4], [5, [6, 7]] ]
#print(x[0][1])
#2

#print(x[2][0])
#5

#print(x[2][1][0])
#6

#print(x[-1][-1][-1])
#7

#x = [ "Hello", ["India", "Python"], [10, [20, 30, [40, 50]]], True ]
#print(x[1][1][0])
#p

#print(x[2][1][2][1])
#50

#SLICING in list

#numbers=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]


#print(numbers[2:8])
#[2,3,4,5,6,7]


#print(f" Slice[2:8]:{numbers[2:8]}")
#Slice[2:8]:[2,3,4,5,6,7]

#print(f"Slice[:5]:{numbers[:5]}")
#Slice[:5]:[0,1,2,3,4]
 
#print(f"Slice[4:]:{numbers[4:]}")
#Slice[4:]: [4,5,6,7,8,9,8,9,10,11,12,13]

#print(f"Slice[:]:{numbers[:]}")
#Slice[:]:[0,1,2,3,4,5,6,7,8,9,10,11,12,13]

#print(f"Slice [::4]:{numbers[::4]}")
#Slice [::4]:[0,4,8,12]

#print(f"Slice[::3]: {numbers[::3]}")
#slice[::3]: [0,3,6,9,12]

#print(f"reverse slice [::-1]: {numbers [::-1]}")
#reverse slice [::-1]: [13,12,11,10,9,8,7,6,5,4,3,2,1,0]

# numbers = [123, 34, 5, 23, 5, 23, 566, 88, 98]
# print(numbers[-3: -8 : -2])
#[556,5,5]

# my_list = ["apple", "banana", "cherry", "date"]


# print(my_list[1][2:4])
#na

# Change a single element
# my_list[1] = "grape"
# print(f"Modified single element: {my_list}") 
#Modified single element:["apple","grape" , "cherry", "date"]

# Change a slice of elements
# my_list[ 0:2 ] = ["mango", "blueberry"]
# print(f"Modified slice: {my_list}") 
#Modified slice:["mango", "blueberry" , "cherry", "date"]

# Change a slice of elements
# my_list[ 0:3 ] = ["mango", "blueberry"]
# print(f"Modified slice: {my_list}") 
#Modified slice:["mango", "blueberry" , "date"]

# my_list[ 0:-1 ] = ["mango", "blueberry"]
# print(f"Modified slice: {my_list}") 
#Modified slice:["mango", "blueberry" , "date"]

# my_list = ["apple", "banana", "cherry", "date"]

# Replace a slice with more or fewer elements (length can change)
# my_list[2:4] = ["mango", "orange", "guava"]
# print(f"Replaced slice with different length: {my_list}") 
#Replaced slice with different length:["apple", "banana","mango", "orange", "guava"]

# Operations

# ADDITION


# list1 = [8, 2, "abc"]
# list2 = [3, 4, "xyz"]

#new list=list1+llist2
# print(f"Concatenated list: {new list}") 
#Concatenated list:[8, 2, "abc",3, 4, "xyz"]


#l1=[23,67,87,"ette"]
#l2=[45,87,56,"praveen"]
#new list=l1+l2
#print(f"combine list: {new list}")
#combine list: [23,67,87,"ette",45,87,56,"praveen"]



## Repetition

#list1=[2,3,4,5]

# repeated_list = list1 * 3
# print(f"Repeated list: {repeated_list}") 
#Repeated list: [2,3,4,5,2,3,4,5,2,3,4,5]


# Comparison

#l1=[2,4,6,"xyz"]
#l2=[2,4,8,"xyz"]

#print(l1>=l2)
#false

# print(l1<=l2)
#true

# print(l1==l2)
# false


# Membership oprator

#list=[2,4,6,8,9,"qwerty"]
#print(f"Is 2 in list? {2 in list}")
#Is 2 in list? true

# print(f"Is 9 in list? {9 in list}")
#Is 9 in list? true

#print(f"Is 5 in list? {5 in list}")
#Is 5 in list? false 


# a = [ 1, 2, 3 , [ 4, 5 ] ]

# print( 2 in a )
#true

# print( 5 in a )
#true

# print( 5 in a[-1] )

#false


# print( [4, 5 ] in a )
#true

# Identity operator
# a = [1,2]
# b = a

# print(a is b)
#false



# Methods:  

#my_list = ["apple", "banana", "cherry", "banana", 123, [1, 2]]

# Append
# my_list.append("date")
# print(my_list)
#["apple", "banana", "cherry", "banana", 123, [1, 2],"date"]


# Insert
#my_list.insert(3, "grape")
#print(f"After insert: {my_list}") 

#After insert: my_list = ["apple", "banana", "cherry","grape", "banana", 123, [1, 2]]


# my_list.insert( -2, "mango")
# print(my_list)
#["apple", "banana", "cherry", "banana", "mango", [1, 2]]


#a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]


#print(a)

#a.append([ 1,2,3,4 ])
#print(a)
#[ 1, 2, 3, 4, 5, 6, 7, 8, 9]
#[1, 2, 3, 4, 5, 6, 7, 8, 9, [1, 2, 3, 4]]

#a.extend([ 1,2,3,4 ])
#print(a)
#[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1,2,3,4 ]

# my_list = ["apple", "banana", "cherry", "banana", 123, [1, 2]]

# Remove


# my_list.remove("apple")

# print(f"After remove: {my_list}") 

#After remove:["banana", "cherry", "banana", 123, [1, 2]]


#my_list = ["apple", "banana", "cherry", "banana"]

#my_list.pop(-1)
#print(my_list)
#["apple", "banana", "cherry",]


















#No Loops Allowed question



#How do you access and print the very last element of a list?
#print(my_list[-1])

#How do you reverse a list without using a loop or .reverse()?
#reverse= my list[::-1]
#print(reverse)

#How do you add a new element to the end of a list?
#list.append()
#print(list)

#How do you find the total number of elements inside a list?
#total=len(list)
#print(total)

#Given a list of numbers, how do you find the sum without using a loop?
#total = sum(numbers)

#How do you find the largest and smallest numbers using built-in functions?
#largest = max(numbers)
#smallest = min(numbers)

#print("Largest number:", largest)
#print("Smallest number:", smallest)

#How do you count how many times the number 5 appears?
#numbers = [5, 10, 5, 20, 5, 30, 5]
#total = numbers.count(5)
#print("Number 5 appears:", total, "times")

#list=[1,3,5,6,8,9]
#newlist=list[:3]
#print(newlist)

#How do you completely empty a list?
#list.clear()

#How do you check if "Python" exists inside a list without loops?
#if "python" in list:
#              print(true)
#else:
#             print(false)



#Basic / Intermediate / Advanced (With Loops) question
#basic question


#Print each element on a new line using a for loop.
#element=[24,56,575,89,97]
#for x in element:
#        print(x)

#Find the sum of all numerical elements using a loop.
#N=[23,67,56,89,56]
#total=0
#for x in N:
#      total=total+x
#print("Sum:",total)


#Find the largest number without using max()
#Number=[23,67,56,89,56]
#largest= Number[0]
#for x in Number:
#         if x>largest:
#             largest=x
#print("largest number:" , largest)


#Count how many times a specific element appears using a loop.
#Number=[25,67,64,67,68,67]
#count=0
#for x in Number:
#          if x==67:
#              count +=1
#print("67 appears:" , count)



#Create a new list containing squares of all numbers from an existing list
#L1=[2,5,7,8,9,1]
#L2=[]
#for x in L1:
#     L2.append(x**2)
#print(L2)


#Intermediate question

#Reverse the elements of a list in-place using a loop.


#Find and print only the even numbers
#number=[1,2,3,4,5,6,7,8,9]
#for x in number:
#        if x % 2 ==0:
#             print(x)

#Remove all duplicate values using a loop.
#A= [10, 20, 10, 30, 20, 40, 50, 30]
#B=[]
#for x in A:
#       if x not in B: 
#            B.append(x)
#print("List without duplicates:", B)


#Check if a specific element exists without using the in keyword.
#List=[2,4,6,7,8,5,]
#suppose we find 6
#S=6
#find=false
#for x in List:
#      if x==S:
#          find= true 
#          break
#if find:
#    print("S exits in List") 
#else:
#    print("S is not exits in List")


#Advanced question 


#





