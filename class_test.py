class MyClass:
    def __init__(self, arg_1, arg_2, arg_3):
        self.x, self._y, self.__z = arg_1, arg_2, arg_3


a = MyClass(1, 2, 3)

print(

    a
)

# class NumOperations(object):
#     def __init__(self, math_list):
#         self.math_list = math_list
#
#     def __sub__(self, other):
#         minuslst = []
#         zipped = zip(self.math_list, other.math_list)
#         for tup in zipped:
#             minuslst.append(tup[0] - tup[1])
#
#         return NumOperations(minuslst)
#
#     def __add__(self, other):
#         addlst = [x + y for x, y in zip(self.math_list, other.math_list)]
#         return NumOperations(addlst)
#
#     def __mul__(self, other):
#         mullst = [x * y for x, y in zip(self.math_list, other.math_list)]
#         return NumOperations(mullst)
#
#     def __repr__(self):
#         return str(self.math_list)
#
#
# x = NumOperations([100, 90, 80, 70, 60])
# y = NumOperations([10, 9, 8, 7, 6])
#
# p = x - y
# z = x + y
# q = x * y
#
# print('Subtraction: ' + str(p))
# print('Addition: ' + str(z))
# print('Multiplication: ' + str(q))

# --------------------------------------------------------------------------------------------


# class MyDictError(Exception):
#     def __init__(self, my_dicy_obj, key, value):
#         self.my_dict_obj = my_dicy_obj
#         self.key = key
#         self.value = value
#
#     def __str__(self):
#         return str(self.value) + ' cannot be added. \nValue has to be an integer less than 50'
#
#
# class MyDict(dict):
#     def __setitem__(self, key, value):
#         if not isinstance(value, int) or value > 50:
#             raise MyDictError(self, key, value)
#         return dict.__setitem__(self, key, value)
#
#
# my_dict_object = MyDict([('a', 80), ('c', 80)])
# print(my_dict_object)

# -----------------------------------------------------------------------------------------------
