def knapsack(W, weights, values):
    # 1. Compute densities
    ratios = [v/w for v, w in zip(values, weights)]
    # print(ratios)
    # 2. Sort items by density
    index = list(range(len(weights)))
    index.sort(key=lambda i: ratios[i], reverse=True)
    print(index)
    max_value = 0
    fractions = [0]*len(weights)

    # 3. Greedily fill knapsack
    for i in index:
        if weights[i] <= W:
            fractions[i] = 1
            max_value += values[i]
            W -= weights[i]
        else:
            fractions[i] = W / weights[i]
            max_value += values[i] * fractions[i]
            break
        print("Taken so far:", fractions)

    # 4. Return total value after loop
    return max_value

# Example usage:
weights = [20, 10, 30]
values  = [100, 60, 120]
capacity = 50

result = knapsack(capacity, weights, values)
print("Max value:", result)
# Expected Max value: 60 + 100 + (20/30)*120 = 240
