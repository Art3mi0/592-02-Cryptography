"""
Author  - Temo Meza
Course  - CSC-592-02
Date    - 10/9/2022
Purpose - Assignment 2
"""

import random
import time

def main():
    message = ""
    flag = True
    while flag:
        message = input("Enter a message to encrypt: ")
        if message == "":
            print("Input can't be empty")
        else:
            flag = False
    encodedString = message.encode()
    print("Message Encoded:", encodedString)
    byteArray = bytearray(encodedString)

    seed = int(time.time())
    random.seed(seed)
    print("Seed being used:", seed)
    key = random.randbytes(len(byteArray))
    print("Key being used:", key)

    cipher = []
    for i in range(len(byteArray)):
        cipher.append(key[i] ^ byteArray[i])
    print("Cypher generated:", bytes(cipher))

    decipher = []
    for i in range(len(cipher)):
        decipher.append(key[i] ^ cipher[i])
    print("Decipher generated:", bytes(decipher))

    print("Decipher decoded:", (bytes(decipher).decode()))

    print()
    flag = True
    repeat = ""
    while flag:
        repeat = input("Enter 1 to encrypt another message or 0 to stop: ")
        if repeat == "1":
            flag = False
            main()
        if repeat == "0":
            flag = False
        else:
            print("Input was not 1 or 0")


main()
