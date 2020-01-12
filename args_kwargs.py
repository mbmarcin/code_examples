def my_func(*args):
    # Iterating over the Python args tuple
    for count, fruit in enumerate(args):
        print('{0}. {1}'.format(count, fruit))


my_func('mango', 'orange', 'apple')


def my_func(**kwargs):
    result = 0
    # Iterating over the Python kwargs dictionary
    for grocery in kwargs.values():
        result += grocery
    return result


print(my_func(bananas=4, cabbage=6, mangoes=7))

# Unpack a list
my_list = ["oranges", "mangoes", "tomatoes", "bananas"]
# print unpacked list
print(*my_list)

my_dict = {"oranges": 4, "mangoes": 5, "tomatoes": 7, "bananas": 6}
# print unpacked dictionary
print(*my_dict)

my_dict = {"oranges": 4, "mangoes": 5, "tomatoes": 7, "bananas": 6}
unpacked_dict = {**my_dict}

# print unpacked dictionary
print(unpacked_dict)

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
final_list = [*list_1, *list_2]

print(final_list, list_1 + list_2)

dict_1 = {"mangoes": 4, "apples": 5, "bananas": 6}
dict_2 = {"lemons": 7, "carrots": "None"}
dict_3 = {"bread": 2, "tomatoes": 15}
final_dict = {**dict_1, **dict_2, **dict_3}

print(final_dict)
