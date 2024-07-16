# initial data
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


# function count
def calculate_structure_sum(data):
    sum_ = 0
    for item in data:
        if isinstance(item, (int, float)):
            sum_ += item
        elif isinstance(item, dict):
            sum_ += calculate_structure_sum(item.values())
            sum_ += calculate_structure_sum(item.keys())
        elif isinstance(item, (list, tuple)):
            sum_ += calculate_structure_sum(item)
        elif isinstance(item, str):
            sum_ += len(item)
        elif isinstance(item, set):
            sum_ += calculate_structure_sum(item)

    return sum_


# main
result = calculate_structure_sum(data_structure)
print(result)
