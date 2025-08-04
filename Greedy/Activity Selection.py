def activity_Selection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    selected = []
    last_finish = -1
    for s, f in activities:
        if s >= last_finish:
            selected.append((s, f))
            last_finish = f
    return selected

s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]

print(activity_Selection(s, f))
