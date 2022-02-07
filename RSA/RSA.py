from RSA import RSA_algo
import random
import time

def do_rsa():
  # STEP 1: two primes p and q to make a modulus of a certain bit length
  bits = 256
  p, q = RSA_algo.generate_2_prime(bits)

  # STEP 2: Modulus is N
  N = p * q;
  print("RSA Bit Length:", N.bit_length())

  # STEP 3: Rest of the public key
  # e must be smaller than this number "smaller":
  smaller = (p - 1) * (q - 1)
  # e must be also be coprime with "smaller"
  e = 0;
  # choose random numbers to select a coprime number
  while(not RSA_algo.is_coprime(e, smaller)):
    e = random.randrange(0, smaller, 1)

  # STEP 4:
  # Private Key
  # d must be e modInverse smaller
  d = pow(e, -1, smaller)

  # message to be encrypted. must be smaller than modulus N
  message = 10
  print("message", message)

  # take the time before both encryption and decryption to calculate total time. (1/2)
  start = time.time()

  message_e = RSA_algo.encrypt(message, e, N)
  print("encrypted", message_e)
  message_d = RSA_algo.decrypt(message_e, d, N)
  print("decrypted", message_d)

  # (2/2)  
  end = time.time()

  print("Time:", "{:f}".format(end - start))

  # log the time in csv file
  RSA_algo.log_data(end - start, bits, "RSA/RSA_Data.csv")
