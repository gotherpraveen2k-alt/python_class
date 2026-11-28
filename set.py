#set 

# Unordered: They don'e have any index values and they do not support slicing.
# Mutable: You can add or remove elements after the set has been created.
# Unique Elements: Every element in a set must be unique. Duplicates are automatically discarded.


# While 1 and True are the same thing
# While 0 and False are the same thing

#sets example

#a = { 123, 324.4 , "2332", (23, 353) }
#print(a)
#{ 123, 324.4 , "2332", (23, 353) }


# a = { False, 0, True, 2, 1, True }
# print(a)
#{False, True, 2}

#a={45,65,true, 1,0, false ,45,78,87,65,98}
#print(a)
#{45,65,true,0,78,87,98}

#creating a empyt list
#empty_list=set()


# a = { 1, 2, 3, 4, 5, 6, 1, 2, "Vipin", "vipin", True, 0, False }
# print(a)
#{ 1, 2, 3, 4, 5, 6, "Vipin", "vipin", 0}


# Creating a set from a list (duplicates are automatically removed)

# a = "Rajasthan"
# my_set = set(a)
# print(my_set)

#{R,a,j,s,t,h,n}

#a="praveen"
#my_set =set(a)
#print(my_set)

#{p,r,a,v,e,n}


# a = (1, 3, 4, 5, 1, 4)
# my_set = set(a)
# print(my_set)

#{1,3,4,5}



# Creating a set directly with curly braces


#fruits = {"apple", "banana", "cherry", "banana", 1, 3, 4, 5, 1}
#print(f"Set of fruits: {fruits}")
#Set of fruits: {1, 3, 4, 5, 'cherry', 'apple', 'banana'}



# dummy = {"x", "t", "a", "A", "X", "T"}
# print(dummy)
#{"x", "t", "a", "A", "X", "T"}


# Set with mixed data types (all elements must be hashable)


#mixed_set = {1, "hello", (1, 2), 3.14, (1, 2)} 
#print(f"Mixed set: {mixed_set}")

#Mixed set: {3.14, 1, (1, 2), 'hello'}


#my_set = {1, 2, 3}
#print(f"Original set: {my_set}")

#{1, 2, 3}


#methods

#.add



#my_set = {1, 2, 3}



# my_set.add((1,2))

#print(my_set)

#{1, 2, 3}



#my_set.add(4)
# print(f"After add(4): {my_set}")

#After add(4):{1, 2, 3 ,4}



# my_set.update((1, 2, 3, 4, 5, 6))
# print(f"{my_set}")

#{1, 2, 3 ,4 ,5 ,6}



# my_set = {1 ,2 ,3}

# my_set.add("abcdefg")
# print(f"{my_set}") 


#{1 , 2, 3, a , b , c , d , e , f , g}


# my_set ={1 , 2, 3,a ,b c,d,e,f,g}

# my_set.add({7,8})
# print(my_set)
#{1 , 2, 3, a ,b , c, d, e, f, g ,7 ,8}



#my_set = {10, 20, 30, 40, 50}


# print(f"Original set: {my_set}")
#Original set: {10, 20, 30, 40, 50}

# my_set.remove(10)
# print(f"{my_set}")
# {20, 30, 40, 50}

#my_set.discard(90)
#print(f"After discard(90): {my_set}")
#After discard(90): {50, 20, 40, 10, 30}

#my_set.discard(20)
#print(f"After discard(20): {my_set}")

#After discard(20) : {50,40, 10, 30}


#.pop  rendomly remove a value 



#my_set = {1 ,2 ,3, "abc", (23)}

#data = my_set.pop()
#print(my_set)
#print(data)

#{1 ,2 ,3, "abc",}
#(23)



#a = { 1, 2, 3 }
#b = a
#a.add(34)
#print(a)
#print(b)

#{ 1, 2, 3 , 34 }
#{ 1, 2, 3 , 34 }



# a = {1, 2, 3}
# b = a.copy()
# b.add(23)
# print(a)
# print(b)

#{1, 2, 3}
#{1, 2, 3, 23}



#.clear


#my_set = {10, 20, 30, 40, 50}
#my_set.clear()
#print(my_set)

#set()

# # Membership oprator 

#my_set={1 ,2, 5, 7, 8}



# print(f"Is 3 in my_set? {3 in my_set}")     
# print(f"Is 6 not in my_set? {6 not in my_set}") 


#Is 3 in my_set? false
#Is 6 not in my_set? true


# print(f"Is 2in my_set? {2 in my_set}")   #
#Is 2in my_set? true

# print(f"Is 8 not in my_set? {8not in my_set}")
#  Is 8 not in my_set?  false

























