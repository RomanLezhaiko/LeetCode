def number_of_steps(num: int) -> int:
    steps = 0
    while num != 0:
        if num % 2 == 0:
            num /= 2   
        else:
            num -= 1

        steps += 1
        
    return steps


print(number_of_steps(1442))
print(number_of_steps(7))
print(number_of_steps(1))