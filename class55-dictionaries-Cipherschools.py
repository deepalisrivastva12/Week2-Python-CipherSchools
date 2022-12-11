user={"name":"Deepali","age":18}
print(user)
print(type(user))
#we can also write dictionaries n diff. manner
user1=dict(name="anushka",age=19)
print(user1)
print(user1["name"])
#we can also make list in dictionaries
user2={
    "name":"Deepali",
    "age":18,
    "fav_drama":["k drama","C drama","webseries"],
    "fav_tune":["awakening","fairy tale"]
}
print(user2["fav_drama"])
#how to add data to an empy dictionaries
user_info={}
user_info["name"]="mohit"
print(user_info)