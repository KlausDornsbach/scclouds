def primes_iterative(n: int) -> list:
    if n <= 1:
        print('invalid input ', n, 'please input a number larger than 1')

    solution = []
    # definimos um array comecando assumindo que todos os numeros sao primos
    is_prime = [True] * n

    for i in range(2, n):
        if not is_prime[i]:
            continue
        
        solution.append(i)

        # se achamos um primo, sabemos que todos os proximos elementos de i em i 
        # sao tambem divisiveis por i, logo nao sao primos  
        for j in range(2*i, n, i):
            #print(j)
            is_prime[j] = False
    
    return solution

print(primes_iterative(2))
print(primes_iterative(3))
print(primes_iterative(4))
print(primes_iterative(5))
print(primes_iterative(6))
print(primes_iterative(7))
print(primes_iterative(8))
print(primes_iterative(16))
print(primes_iterative(32))