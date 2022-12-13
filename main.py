# #A list comprehension works as following:
#
# #with a for loop looks like that:
# numbers = [1, 2, 3]
# new_list = []
# for n in list:
#     add_1 = n + 1
#
# new_list.append(add_1)
#
# #with list comprehension looks like the following
# #Example code
# new_list = [new_item for item in list]
# #on the example above
# new_list = [n+1 for n in numbers]

print([num * 2 for num in range(1,5)])

# there is also Conditional list comprehension
# new_itemlist = [new_item for item in list if test]
# Example
names =["Alex", "Billy", "Chris", "Steve", "Maik","Nikolai"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
print([name.upper() for name in names if len(name) > 5])