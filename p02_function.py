# Python p02. function practice
# reference: https://www.kancloud.cn/thinkphp/python-tutorial/37563
# -------------------------------------------------------------------
def print_id(arg):
    name = '[unknown name]'
    for k,v in globals().items():
        if v == arg:
            name = k
    print('id of {}: {}'.format(name, id(arg)))

# 1. 默認值
print('''\n\
------------------------
 #1
 Function 之 默認值
 mutable vs. immutable objects
------------------------\
''')
# 1.1 immutable
i = 5
print("\n1.1 Immutable Object 'i={}' in function f(arg=i)".format(i))
print_id(i)

def f_immutable(arg=i):
    print('>>> f(): arg = {}'.format(arg))
    print('id of arg: {}'.format(id(arg)))


i = 6
print('>> Assign 6 to "i", i = {}'.format(i))
print_id(i)

f_immutable()
print('[CONCLUSION] "arg" inside f() is not changed! Immutable object "arg"(int) was assigned as a value')



# 1.2 mutable
i = [1]
print("\n1.2 Mutable Object 'i={}' in function f(arg=i)".format(i))
print_id(i)

def f_mutable(arg=i):
    print('>>> f(): arg = {}'.format(arg))
    print('id of arg: {}'.format(id(arg)))


i.append(2)
print('>> Append 2 into "i", i = {}'.format(i))
print_id(i)
f_mutable()
print('[CONCLUSION] "arg" inside f() is changed! Mutable object "arg"(lists) was assigned as an address(id)')


# 若不想默認值一直被累積修改，應改用以下方法
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
