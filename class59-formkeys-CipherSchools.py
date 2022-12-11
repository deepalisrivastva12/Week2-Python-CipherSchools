user2={
    "name":"Anushka",
    "height":"unknown",
    "weight":"unknown",
    "age":"unknown"
}
d=dict.fromkeys(("height","weight","age"),"unknown")# we can also give it a range
print(d)
#get method
print(user2["name"])#output=anushka
print(user2.get("names"))#by using 'get' it will not give us an error
print(user2.get("names","not found!"))