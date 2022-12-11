#generate a list of the square of the no. from 1 to 10
def square_list(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square
numbers=list(range(1,11))
print(square_list(numbers))
#print the reverse of the numbers by suing append or reverse method 
def number_list(l):
    numbers=[]
    for i in range(len(l)):
        r_numbers=l.pop()
        numbers.append(r_numbers)
    return numbers
digit=[1,2,3,4,5]
print(number_list(digit))
#print the revrerse order of the list like ["xyz","pql","stw"]
def abc_alphabet(l):
    alphabet=[]
    for i in l:
        alphabet.append(i[::-1])
    return alphabet
abc=["xyz","tuv","stw"]
print(abc_alphabet(abc))
#filter the odd and even elements in a list
def odd_even(l):
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            odd.append(i)
        else:
            even.append(i)
    output=(even,odd)
    return output
numbers=[1,2,3,4,5,6,7]
print(odd_even(numbers))
#print the elememts which is preent in both list
def common_list(l1,l2):
    l=[]
    for i in l1:
        if i in l2:
            l.append(i)
    return l
print(common_list([1,4,6,8,7,6,3],[1,2,3,4,5,6]))
#how to count the no.s of lists which is present in another list
numbers=[1,2,3,[1,2,3,],[5,6,7],[4,5]]
def number_of(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count
print(number_of(numbers))
        