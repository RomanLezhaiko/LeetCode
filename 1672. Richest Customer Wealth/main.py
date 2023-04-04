def maximum_wealth(accounts: list) -> int:
    max = 0
    for i in range(0, len(accounts)):
        if max < sum(accounts[i]):
            max = sum(accounts[i])
        
    return max


print(maximum_wealth([[1, 2, 3], [2, 6, 7]]))
print(maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))