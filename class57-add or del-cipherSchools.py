user2={
    "name":"Deepali",
    "age":18,
    "fav_drama":["k drama","C drama","webseries"],
    "fav_tune":["awakening","fairy tale"]
}
#to add on the element in dictionaries
user2["fav_song"]=["dreamers","pink venom"]
print(user2)
#to del the element from dictionaries 
popped_item=user2.pop("fav_tune")
print("the popped item is:",(popped_item))
print(user2)
#to remove random element
popped_item1=user2.popitem()
print(user2)
print("the pooped item is: ",(popped_item1))
#how to update the element of dictionaries 
user2={
    "name":"Deepali",
    "age":18,
    "fav_drama":["k drama","C drama","webseries"],
    "fav_tune":["awakening","fairy tale"]
}
user3={"name":"Deepali Srivastava","Course":"Btech(CSE)"}
user2.update(user3)
print(user2)