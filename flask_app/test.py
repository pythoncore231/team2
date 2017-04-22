def add(param1, param2):
    mi = -100
    ma = 1000
    total = 0

    if mi <= param1 <= ma and mi <= param2 <= ma:
        total = param1 + param2
    print total
    return total
