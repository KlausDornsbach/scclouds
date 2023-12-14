def fibonacci(n: int) -> int:
    if n < 0:
        print('invalid input ', n, 'please input a number larger than or equal to 0')

    def fibonacci_recursive(n: int) -> int:
        if n == 1 or n == 0:
            return 1

        return fibonacci_recursive(n-1) + fibonacci_recursive(n - 2)
    
    return fibonacci_recursive(n)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(16))
print(fibonacci(32))

