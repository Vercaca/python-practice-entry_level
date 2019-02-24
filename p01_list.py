# Python p01. LIST practice
# -- Here will show you some tricky usages of LIST
# reference: https://www.kancloud.cn/thinkphp/python-tutorial/37551

# ======================================
# Content
# ======================================
# 1. slice    l[X:Y]
#    insert / delete / remove / clear / reverse
# 2. mutable object
#
# 3. Performance Comparison
#
# 4. List Comprehension
#
# 5. Lambda Function
# -------------------------------------------------------------------

from pprint import pprint

ORIGINAL_LIST = [1, 2, 3, 4]


class BasePractice:
    counter = 0
    var = []
    def __init__(self, titles=[], var=None):
        self.reduce_variable(var)
        BasePractice.counter += 1
        self.counter = BasePractice.counter
        print("\n" + self.get_title(titles))


    def reduce_variable(self, var):
        if var is None:
            return None

        self.var = var[:] # copy var list
        print('Original list: {}'.format(self.var))

        return None

    def test(self):
        ## do_something()
        return None

    def get_title(self, titles):
        print_titles = ['='*60, '-'*40]
        print_titles[1:1] = ['# {}'.format(self.counter)]
        print_titles[2:2] = titles
        strs_title = '\n'.join(print_titles)
        return strs_title


class SliceUsage(BasePractice):
    def __init__(self):
        titles = ["LIST 的 SLICE 用法 a[x:y]", "insert / delete / clear"]
        super().__init__(titles, ORIGINAL_LIST)

    def test(self):
        self.insert_elements(eles = [9, 10, 11], pos = 1)
        self.delete_elements(start_pos=1, end_pos=4)
        self.clear()
        return

    def insert_elements(self, eles, pos):
        self.var[pos:pos] = eles
        print("\n[INSERT] a[{}:{}] = {}".format(pos,pos, eles))
        print('After inserting values(list) into list: \n{}'.format(self.var))
        ## [1, 2, 3, 4] --> [1, 9, 10, 11, 2, 3, 4]
        return
    def delete_elements(self, start_pos, end_pos):
        self.var[start_pos:end_pos] = []
        print("\n[DELETE] a[{}:{}] = []".format(start_pos, end_pos))
        print('After deleting values(list) from list: \n{}'.format(self.var))
        ## [1, 9, 10, 11, 2, 3, 4] --> [1, 2, 3, 4]
        return
    def clear(self):
        self.var[:] = []
        print("\n[CLEAR] a[:] = []")
        print('After clear the list: \n{}'.format(self.var))
        ## [1, 2, 3, 4] --> []
        return


class MutableObjectCharacteristic(BasePractice):
    def __init__(self):
        titles = ["MUTABLE OBJECT -- LIST", "以變數之地址回傳給對象"]
        super().__init__(titles, ORIGINAL_LIST)

    def test(self):
        self.slice_copy_test()

    def slice_copy_test(self):
        # slice as a copy
        b = self.var[:]
        b.append(5)
        print('\n- Slice a[:] will return as a copy of "a" \n{}'.format(b))
        print('As a result, list "a" will not be changed, a: \n{}'.format(self.var))
        ## b = [1, 2, 3, 4, 5], a = [1, 2, 3, 4]

    def call_by_reference(self):
        # call by reference
        c = self.var
        c.append(5)
        print('\n- List is a mutable object, "c" points to "a" \n{}'.format(b))
        print('In this way, list "a" will be changed, a: \n{}'.format(self.var))
        ## c = [1, 2, 3, 4, 5], a = [1, 2, 3, 4, 4]

class PerformanceComparison(BasePractice):
    def __init__(self):
        titles = ["list() vs. []", "效能與pitfalls"]
        super().__init__(titles)

    def test(self):
        self.time()
        self.usage()
        self.pitfall()

    def time(self):
        print('\n3.1 效能')
        from timeit import timeit
        print('Time used of list(): {}'.format(timeit("list()")))
        print('Time used of []: {}'.format(timeit("[]")))
        print('[CONCLUSION] [] faster than list()')
        return

    def usage(self):
        print('\n3.2 用途')
        print('• list() creates list from the same iterable')
        print('• [] stores the iterable object')
        print('\n3.2.1 pitfall 01 -- with dict(sth)')
        sth = [(1, 2), (3, 4), (5, 6)]
        sth2 = list(dict(sth))
        print('sth2 = list(dict(sth)), result: {}'.format(sth2))
        sth3 = [dict(sth)]
        print('sth3 = [dict(sth)], result: {}'.format(sth3))
        return

    def pitfall(self):
        print('\n3.2.2 pitfall 02 -- with map(sth)')
        sth = [(1, 2), (3, 4), (5, 6)]
        sth2 = list(map(lambda x:x[1], sth))
        print('sth2 = list(map(lambda x:x[1], sth))), result: {}'.format(sth2))
        sth3 = [map(lambda x:x[1], sth)]
        print('sth3 = [map(lambda x:x[1], sth)], result: {}'.format(sth3))
        return


class ListComprehension(BasePractice):
    def __init__(self):
        titles = ["list Comprehension", "單行"]
        super().__init__(titles)

    def test(self):
        self.as_single_form()
        self.as_nested_form()
        self.flatten()
        return
    def as_single_form(self):

        print('4.1 list comphension example:')
        print('>>> [x**2 for x in range(10)]')
        comp_list = [x**2 for x in range(10)]
        print(comp_list)
        return

    def as_nested_form(self):
        matrix = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
        print('\n4.2 nested list comphension example:')
        print('''>>> matrix = [
                [1,2,3],
                [4,5,6],
                [7,8,9]]''')
        print('>>> [[row[i] for row in matrix] for i in range(len(matrix[0]))]')
        nested_list = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
        pprint(nested_list)

        print('\nOr with zip()...')
        print('>>> list(zip(*matrix))')
        nested_list = list(zip(*matrix))
        print(nested_list)
        return

    def flatten(self):
        print('\n4.3 flatten a list using a listcomp with two "for"')
        print('>>> vec = [[1,2,3], [4,5,6], [7,8,9]]')
        print('>>> [num for row in vec for num in row]')
        vec = [[1,2,3], [4,5,6], [7,8,9]]
        result_list = [num for row in vec for num in row]
        print(result_list)
        return


class LambdaFunction(BasePractice):
    def __init__(self):
        titles = ["Lambda function (匿名函數)"]
        super().__init__(titles)

    def test(self):
        l = (lambda x: x + 1)(3)
        print('>>> (lambda x: x + 1)(3)')
        print(l)
        return


def main():
    # 1. try SLICE
    SliceUsage().test()

    # 2. Mutable Object Characteristic
    MutableObjectCharacteristic().test()

    # 3. Performance 效能比較
    PerformanceComparison().test()

    # 4. List comprehension
    ListComprehension().test()

    # 5. lambda
    LambdaFunction().test()

if __name__ == '__main__':
    main()
