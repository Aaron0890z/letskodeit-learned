this_list = ['a', 45, 'c', 3.9, 'd', 5, 'u', 8]

print(this_list)

a = len(this_list)
print(a)

print(this_list[2])

print(type(this_list))

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

print(this_list[2:])

if 'a' in this_list:
    print("a is present")

this_list[2] = [77]
print(this_list)

this_list[2:3] = [77]
print(this_list)

this_list.insert(4, 'p')
print(this_list)

this_list.append(99)
print(this_list)

that_list = (22, 33, 44, 66)

this_list.extend(that_list)     # can append tuples, dicts, sets
print(this_list)

this_list.pop(-1)
print(this_list)

this_list.remove(99)
print(this_list)

del this_list[-3]       # del this_list to del whole list/ this.clear() to clear the list
print(this_list)

for x in this_list:
    print(x, end="-")