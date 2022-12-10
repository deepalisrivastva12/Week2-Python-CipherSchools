# lists 
number=[1,3,2,4,5,6,7,8]
print (number)

#how we can change the items of lists with another variable
mixed =["name","class","section",1,3,4,5.5]
mixed[0:1]=["sita","1"]
print(mixed)

#how to add the items in a list 
fruits=["mango","orange","apple","banana","kiwi"]
fruits.append("pineapple")
print(fruits)
#how to add two lists 
basket1=["mango","orange","apple","banana","kiwi"]
basket2=["patato","tomato","pumpkin"]
basket1.extend(basket2)
print(basket1)
#how to insert the items in  a list in our desire position
fruits=["mango","orange","apple","banana","kiwi"]
fruits.insert(3,"pineapple")
print(fruits)
#how to delte the items from lits
fruits=["mango","orange","apple","banana","kiwi"]
fruits.pop(3)
print(fruits)
#how to delete the items from list by using del operater
fruits=["mango","orange","apple","banana","kiwi"]
del fruits[4]
print(fruits)
#how to remove the repeated item from the lists
fruits=["mango","orange","apple","banana","kiwi","mango"]
fruits.remove("mango")
print(fruits)
#how to check  the particular element is present in list or not
fruits=["mango","orange","apple","banana","kiwi"]
if "orange" in fruits:
    print("orange is present")
else:
    print("orange is not present")
#how to count the no. of the particular item which is repeated
fruits=["mango","orange","pineapple","banana","mango","kiwi","mango","mango","pineapple","banana"]
print(fruits.count("mango"))
# how to arrange the order alphabetically 
fruits=["mango","orange","pineapple","banana","mango","kiwi","mango","mango","pineapple","banana","apple"]
fruits.sort()
print(fruits)# this method is also apply for the numbers
#how to copy the lists
fruits=["mango","orange","pineapple","banana","mango","kiwi","mango","mango","pineapple","banana"]
copy_lists=fruits.copy()
print(copy_lists)
# how to clear the list
fruits=["mango","orange","pineapple","banana","mango","kiwi","mango","mango","pineapple","banana"]
fruits.clear()
print(fruits)
#list inside list
a=[[1,2,3],[4,5,6],[7,8,9]]
for i in a:
    print(i)
# how to get the elements of sublists also 
a=[[1,2,3],[4,5,6],[7,8,9]]
for sublist in a:
    for i in sublist:
        print(i)
#how to get the particular element in this type of inside list 
a=[[1,2,3],[4,5,6],[7,8,9]]
print(a[1][0])