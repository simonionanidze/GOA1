import numbers


def my_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer

    for element in it:
        value = func(value, element)
    
    return value

# გამოყენება ჩვენი my_reduce ფუნქციის
my_sum_result = my_reduce(lambda x, y: x + y, numbers)
print("ჯამი (my_reduce):", my_sum_result)

my_product_result = my_reduce(lambda x, y: x * y, numbers)
print("ნამრავლი (my_reduce):", my_product_result)
