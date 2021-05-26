import csv
import sys
import os

def generate_prime_file():
    write_file = open("primes.txt","a+")

    for i in range(2,100000):
        isprime = True
        for j in range(2,i):
            if i%j == 0:
                isprime = False
                break
        if isprime:
            write_file.write("{},".format(i))

print(sys.maxsize)
generate_prime_file()
        

