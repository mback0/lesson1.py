my_list_1 = list(range(1,1000, 2))
my_list_2 = []
for i in my_list_1:
    cube = i**3
    my_list_2.append(cube)
print(my_list_2)
my_list_3 = []
for i2 in my_list_2:
    plus = i2+17
    my_list_3.append(plus)
print(my_list_3)


def sum_list_1(dataset: list):
    final_sum = 0
    for j in dataset:
        sum_in_element = 0
        to_string = str(j)
        for x in to_string:
            to_int = int(x)
            sum_in_element += to_int
        if sum_in_element % 7 == 0:
            final_sum += sum_in_element
    return final_sum

result = sum_list_1(my_list_3)
print(result)
