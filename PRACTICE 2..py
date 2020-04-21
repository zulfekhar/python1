import math
name = 'VIZARTS'
mylist = []
for letter in name:
    mylist.append(letter)
print(mylist)


mynewlist = [letter for letter in name]
print(mynewlist)

list_1 = [num for num in range(1,101)]
print(list_1)

list_comp = [1,2,3,4,5,6,7,8,9]
sec_list = []
for num in list_comp:
    sec_list.append(num)
print('sec list is :', sec_list) 

sec_list = [num for num in list_comp]
print(sec_list)