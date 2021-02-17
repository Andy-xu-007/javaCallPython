import copy

lst = [1,3,5,[2,4]]

lst1 = lst[:]
lst1[0] = 3
print(lst1[0], lst[0])

lst2 = list(lst)
lst2[1] = 0
print(lst2[1],lst[1])

lst3 = lst.copy()
lst3[2] = 0
print(lst3[2],lst[2])

lst4 = copy.copy(lst)
lst4.append(4)
print(lst4[-1],lst[-1])

# deep copy
lst5 = copy.deepcopy(lst)
lst5.append(5)
print(lst5[-1],lst[-1])

lst6 = lst
lst6.append(6)
print(lst6[-1], lst[-1])

