"""
Author  - Temo Meza
Course  - CSC-592-02
Date    - 9/26/2022
Purpose - Assignment 1
"""

import random

"""
input   -   string
output  -   int 1, 2, or 0
purpose -   Method determines whether inputted character is a
            letter, and returns a value indicating 1 for a capital,
            2 for a lowercase, and 0 for a non-letter character     
"""
def letterCheck(l):
    if (ord(l) >= 65) and (ord(l) <= 90):
        return 1    # 1 means capital letter
    elif (ord(l) >= 97) and (ord(l) <= 122):
        return 2    # 2 means lowercase letter
    else:
        return 0    # 0 means not a letter


"""
input   -   int
output  -   string
purpose -   Method generates and returns a random string of only 
            capital letters of inputted length    
"""
def keyGenerator(length):
    key = ""
    while len(key) != length:
        key += chr(random.randint(65, 90))
    return key


"""
input   -   string, string
output  -   string
purpose -   Method takes a key string and a message string and 
            applies the Vigenere Cipher to encrypt the message.
            The output is an encrypted version of the inputted message.
"""
def encrypt(key, message):
    cipher = ""         # Initialize variables
    fullKey = ""

    while len(fullKey) != len(message):     # Algorithm for extending
        temp = len(message) - len(fullKey)  # the key to match the
        if temp < len(key):                 # message length
            fullKey += key[:temp]
        else:
            fullKey += key

    for i in range(len(message)):
        if letterCheck(message[i]) == 0:                    # 64 is subtracted because
            cipher += message[i]                            # the key is generated with
        elif letterCheck(message[i]) == 1:                  # only capital letters.
            temp = ord(message[i]) + ord(fullKey[i]) - 64   # The unicode of A is 65,
            if temp > 90:                                   # so subtracting will result
                temp -= 26                                  # with values 1-26.
            cipher += chr(temp)                             # 26 is subtracted when a
        else:                                               # character passes Z or z and
            temp = ord(message[i]) + ord(fullKey[i]) - 64   # returns back to the beginning.
            if temp > 122:
                temp -= 26
            cipher += chr(temp)

    return cipher


"""
input   -   string, string
output  -   string
purpose -   Method takes a key string and a cipher string and 
            uses the Vigenere Cipher to decrypt the message.
            The output is a decrypted version of the inputted cipher.
"""
def decrypt(key, cipher):
    message = ""
    fullKey = ""

    while len(fullKey) != len(cipher):      # Algorithm for extending
        temp = len(cipher) - len(fullKey)   # the key to match the
        if temp < len(key):                 # message length
            fullKey += key[:temp]
        else:
            fullKey += key

    for i in range(len(fullKey)):                       # Refer to encrypt method for
        if letterCheck(cipher[i]) == 0:                 # explanation. Similar but reversed
            message += cipher[i]
        elif letterCheck(cipher[i]) == 1:
            temp = ord(cipher[i]) - ord(fullKey[i]) + 64
            if temp < 65:
                temp += 26
            message += chr(temp)
        else:
            temp = ord(cipher[i]) - ord(fullKey[i]) + 64
            if temp < 97:
                temp += 26
            message += chr(temp)
    return message


"""
input   -   None
output  -   None
purpose -   The method for taking in and checking an input from the user.
            This method is separate from main because I was gonna have 
            the program start over but no longer feel like implementing
            that.
"""
def start():
    # Instructions
    print("This program will encrypt a html file using Vigenere Cipher")
    print("This program will generate 1 txt file and 2 html files")
    print("In order for the program to work, ensure the html file"
          "that is being encrypted is located in the same folder "
          "as this program")
    print()

    flag = False
    filePath = ""
    while not flag:
        filePath = input("Enter the name of the html file (Without the \".html\" end): ")
        try:
            filePath += ".html"         # A loop asking for a user's file
            test = open(filePath, "r")  # and repeats until the user inputs
            flag = True                 # one that exists
            test.close()
        except:
            print("ERROR: File missing or does not exist")

    length = ""
    while not length.isdigit():
        length = input("Enter desired length of key: ")
        if length.isdigit():        # A loop for accepting a valid
            if int(length) <= 1:    # length from the user
                length = ""
                print("ERROR: integer can not be 1 or less")
        else:
            print("ERROR: integer not entered")

    generateFiles(filePath, int(length))    # A separate method in case I wanted the program to
                                            # start over. I think keeping everything together would
                                            # have resulted in a recusrsion error.

"""
input   -   String, String
output  -   None
purpose -   This method generates 3 files depending on the inputs
            from the start method
"""
def generateFiles(file, length):
    print("Generating key file...")
    tempKey = keyGenerator(length)
    keyFile = open("key.html", "w")     # Key file generation
    for j in tempKey:
        keyFile.write(j)
    keyFile.close()

    print("Generating encoded html file...")

    fileText = ""
    with open(file, "r") as tempFile:   # Putting everything from the
        line = tempFile.readline()      # html file into a single
        while line != '':               # python string object
            fileText += line
            line = tempFile.readline()

    fileKey = ""
    with open("key.html", "r") as tempFile: # Reading the generated key
        line = tempFile.readline()          # file
        while line != '':
            fileKey += line
            line = tempFile.readline()

    fileEncrypt = encrypt(fileKey, fileText)
    encryptFileName = file[:-5] + "_end.html"
    encryptFile = open(encryptFileName, "w")    # Generating the encrypted
    for j in fileEncrypt:                       # file
        encryptFile.write(j)
    encryptFile.close()

    encryptText = ""
    with open(encryptFileName, "r") as readFile:    # Reading the encrypted
        line = readFile.readline()                  # file and placing
        while line != '':                           # everything into a
            encryptText += line                     # string object
            line = readFile.readline()

    print("Generating decrytpted file...")
    fileDecryptText = decrypt(fileKey, encryptText)
    decryptFileName = file[:-5] + "_dec.html"
    decryptFile = open(decryptFileName, "w")    # Generating the decrypted
    for j in fileDecryptText:                   # file
        decryptFile.write(j)
    decryptFile.close()
    print("done")


def main():
    start()


main()