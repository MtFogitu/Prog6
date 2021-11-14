def merge(lists):
    lists_0 = sum(lists, [])
    scope = max(lists_0) + 1
    C = [0] * scope
    for x in lists_0:
        C[x] += 1
    lists_0[:] = []
    for number in range(scope):
        lists_0 += [number] * C[number]
    print(lists_0)

