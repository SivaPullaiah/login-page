# create a set
py_set_num = {3, 7, 11, 15}
print(py_set_num)

#create a set of mixed datatypes
py_set_num = {11, 1.1, "11", (1,2)}
print(py_set_num)

#set can't store duplicate elements
py_set = {3, 7, 11, 15, 3, 7}
print(py_set)

#create a set using the set() method
#create a set with fixed set of elements
py_set_mix = set([11, 1.1, "11", (1,2)])
print(py_set_mix)

#creating set with dynamic elements
py_list = [11, 1.1, "11", (1,2)]
py_list.append(12)
print(py_list)
py_set_mix = set(py_list)
print(py_set_mix)

#let's try to create an empty python set
py_set_num = {}
print(py_set_num)
print(type(py_set_num))

py_set_num = set()
print(py_set_num)
print(type(py_set_num))

#let's try to change a python set
py_set_num = {77, 88}
try:
    print(py_set_num[0])
except Exception as ex:
    print(ex)
    print(py_set_num)
    
#let's add an element to the set
py_set_num.add(99)
print(py_set_num)

#let's add multiple elements to the set
py_set_num.update([44, 55, 66])
print(py_set_num)

#let's add a list and a set as elements
py_set_num.update([4.4, 5.5, 6.6], {2.2, 4.4, 6.6})
print(py_set_num)

#let's try to use a python set
py_set_num = {22, 33, 55, 77, 99}
#discard an element from the set
py_set_num.discard(99)
print(py_set_num)

#remove an element from the set
py_set_num.remove(77)
print(py_set_num)

#discard an element not present in the set
py_set_num.discard(44)
print(py_set_num)

#remove an element not present in the set
try:
    py_set_num.remove(44)
except Exception as ex:
    print("keyerror:", ex)
    
#let's use the following python set
py_set_num = {22, 33, 55, 77, 99}
print(py_set_num)

#pop an element from the set
py_set_num.pop()
print(py_set_num)

#pop one more element from the set
py_set_num.pop()
print(py_set_num)

#clear all elements from the set
py_set_num.clear()
print(py_set_num)