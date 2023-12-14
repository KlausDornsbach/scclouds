def primes(n: int) -> list:
    if n <= 1:
        print('invalid input ', n, 'please input a number larger than 1')

    mem = []
    def primes_recursive(n: int, stop: int) -> int:
        if n > stop:
            return
        
        primes_recursive(n+1, stop)
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return
        
        mem.append(n)
    
    primes_recursive(2, n)
    return mem

# esse algoritmo foi feito com base em DFS entao a ordem é reversa
print(primes(2))
print(primes(3))
print(primes(4))
print(primes(5))
print(primes(6))
print(primes(7))
print(primes(8))
print(primes(16))
print(primes(32))