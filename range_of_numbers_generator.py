# freeCodeCamp recursion lab


def range_of_numbers(start_num, end_num):
    if end_num < start_num:
        return []
    count_list = range_of_numbers(start_num, end_num - 1)
    count_list.append(end_num)
    return count_list


# other exercises


def range_of_numbers_upwards(start, end):
    if start > end:
        return []
    list = range_of_numbers_upwards(start + 1, end)
    list.append(start)
    return list


def power(num):
    if num == 1:
        return 1
    return num * power(num - 1)


def fibonacci(num):  # returns nth element in the fibonacci sequence
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == "__main__":
    print(range_of_numbers_upwards(1, 15))
    print(power(5))
    print(fibonacci(5))
