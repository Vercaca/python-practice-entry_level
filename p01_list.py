# Python p01. list practice
# reference: https://www.kancloud.cn/thinkphp/python-tutorial/37551
# -------------------------------------------------------------------

def get_original_a():
    a = [1,2,3,4]
    return a

a = get_original_a()
print('Original list a: {}'.format(a))

# 1. slice [X:X]
print('''\n\
------------------------
 LIST 的 SLICE 用法 a[x:y]
 insert / delete / remove
------------------------\
''')
# insert
a[1:1] = [9, 10, 11]
print("\n[INSERT] a[1:1] = [9, 10, 11]")
print('After inserting values(list) into list: \n{}'.format(a))


# delete / remove
a[1:4] = []
print("\n[DELETE] a[1:4] = []")
print('After deleting values(list) from list: \n{}'.format(a))

# clear the list
a[:] = []
print("\n[CLEAR] a[:] = []")
print('After clear the list: \n{}'.format(a))


# 2. mutable object
print('''\n\
------------------------
 MUTABLE OBJECT -- LIST
 以變數之地址回傳給對象
------------------------\
''')
a = get_original_a()

# slice as a copy
b = a[:]
b.append(4)
print('\n- Slice a[:] will return as a copy of "a" \n{}'.format(b))
print('As a result, list "a" will not be changed, a: \n{}'.format(a))

#
c = a
c.append(4)
print('\n- List is a mutable object, "c" points to "a" \n{}'.format(b))
print('In this way, list "a" will be changed, a: \n{}'.format(a))
