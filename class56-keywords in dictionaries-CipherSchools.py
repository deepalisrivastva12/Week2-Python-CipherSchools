#check the function is present or not present 
user2={
    "name":"Deepali",
    "age":18,
    "fav_drama":["k drama","C drama","webseries"],
    "fav_tune":["awakening","fairy tale"]
}
if "Deepali" in user2.values():#for the values
    print("present")
else:
    ("not present")
if "fav_drama" in user2:#for the keyword
    print("present")
else:
    ("not present")
#loop in dictionaries
for i in user2:#keywords
    print(i)
print("\n")
for i in user2.values():#values
    print(i)
#or
for i in user2:#values
    print(user2[i])
#item methods
user=user2.items()
print(user)
