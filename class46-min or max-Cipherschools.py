numbers=[20,30,40,69,-2]
print(min(numbers))
print(max(numbers))
# #how to get the greatest diff between the numbers
print(max(numbers)-min(numbers))
#or we can also done this by using def
def greatest_diff(l):
    return max(l)-min(l)
print(greatest_diff(numbers))