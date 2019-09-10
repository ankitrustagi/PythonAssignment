import math 
import time 
"""
Find the sum of all the primes below 200,000. (e.g. The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17 )
"""
def is_prime(n): 
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = int(math.floor(math.sqrt(n)))
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True
  

total = 0
if __name__ == "__main__":
    for num in range(1,200000): 
        prime_num = is_prime(num) 
        total += prime_num 
    print("Total prime numbers in range :", total) 
