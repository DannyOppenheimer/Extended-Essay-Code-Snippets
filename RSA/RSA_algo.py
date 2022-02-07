import random
import math

# Check if numbers are coprime (they share no common factors except 1)
def is_coprime(x, y):
    return math.gcd(x, y) == 1

# Encrypt parameter "cipher" with private key e and modulus N
def encrypt(cipher, e, N):
  return pow(cipher, e, N)

# Decrypt parameter "cipher" with private key e and modulus N
def decrypt(cipher, d, N):
  return pow(cipher, d, N)

# Generate 2 random prime numbers that will multiply together to achieve the desired bit length
def generate_2_prime(n):
  n1 = n / 2
  n1 = int(n1)
  prime1 = 0
  prime2 = 0

  while (prime1 * prime2).bit_length() != n:
    prime1 = 0
    prime2 = 0
    while not is_prime(prime1):
      prime1 = random.randrange(2 ** (n1 - 1) + 1, 2 ** n1 - 1)
    while not is_prime(prime2):
      prime2 = random.randrange(2 ** (n1 - 1) + 1, 2 ** n1 - 1)

  return prime1, prime2
  
# Test if a number is prime
# n = number to test, k = number of tests to do
def is_prime(n, k=128):
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

# Log the time it takes for a 
def log_data(time, bits, name): 
  with open(name, "a") as f:
    f.write("\n" + f"{bits}," + "{:f}".format(time))
