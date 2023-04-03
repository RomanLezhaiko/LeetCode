def fizz_buzz(n: int) -> list:
    lst = []
    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            lst.append("FizzBuzz") 
        elif i % 3 == 0:
            lst.append("Fizz")
        elif i % 5 == 0:
            lst.append("Buzz")
        else:
            lst.append(str(i))
        
    return lst


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))