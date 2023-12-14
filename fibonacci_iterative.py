def fibonacci(n: int) -> int:
    if n < 0:
        print('invalid input ', n, 'please input a number larger than or equal to 0')
    
    memory = [None] * n
    if n <= 1:
        return 1
    
    memory[0] = 1
    memory[1] = 1

    for i in range(2, n):
        memory[i] = memory[i-1] + memory[i-2]
    
    return memory[-1]

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