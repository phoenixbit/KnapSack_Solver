# this code is to print out the best case items in a knapsack using dynamic programming

from collections import namedtuple
from typing import List, Any

Item = namedtuple("Item", ['index', 'value', 'weight'])
items = []
best_ans = []

def line_receiver(input_data, n):
    for i in range(1, n+1):
        items.append(Item(i - 1, int(input_data[i][0]), int(input_data[i][1])))
    return items


def solve_it(input_data):
    global best_ans
    item_count = int(input_data[0][0])  # n
    capacity = int(input_data[0][1])  # k
    index = 0
    line_receiver(input_data, item_count)
    dynamic_list = []
    best_ans = []
    best_ans = best_ans_dummy_setter()
    ksPowerPrinter(0, len(items), dynamic_list, capacity)
    print(best_ans)


def sum_weight(dynamic_list):
    sumVal = 0
    for obj in dynamic_list:
        sumVal += obj.weight
    return sumVal


def sum_value(dynamic_list):
    sumVal = 0
    for obj in dynamic_list:
        sumVal += obj.value
    return sumVal

def best_ans_dummy_setter():
    global items
    global best_ans
    for i in range(len(items)):
        best_ans.append(Item(0,0,999))
    return best_ans


def ksPowerPrinter(i, n, dynamic_list, capacity):
    global best_ans
    if i == n:
        return

    for p in range(i, n):
        dynamic_list.append(items[p])
        if (sum_weight(dynamic_list) <= capacity):
            if (sum_value(dynamic_list) > sum_value(best_ans)):
                best_ans = dynamic_list.copy()

        ksPowerPrinter(p + 1, n, dynamic_list, capacity)
        del dynamic_list[len(dynamic_list) - 1]
    return


if __name__ == '__main__':
    input_data = [[4,10],[7,3],[10,5],[10,5],[13,8]]
    solve_it(input_data)
    input_data1 = [[4,10],[7,3],[10,5],[10,5],[14,7]]
    solve_it(input_data1)
