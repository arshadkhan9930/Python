test_list = [[1, 0, -1], [-1, 0, 1], [-1, 0, 1], [1, 2, 3], [3, 4, 1]]

res = list(set(tuple(sorted(sub)) for sub in test_list))

print(res)
