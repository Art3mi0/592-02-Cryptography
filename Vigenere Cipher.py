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


def start(again):
    if not again:
        print("This program will encrypt a html file using Vigenere Cipher")
        print("This program will generate 1 txt file and 2 html files")
        print("In order for the program to work, ensure the html file"
              "that is being encrypted is located in the same folder "
              "as this program")

    flag = False
    while flag:
        filePath = input("Enter the name of the html file (Without the \".html\" end)") + ".html"
        try:
            test = open(filePath, "r")
            flag = True
            test.close()
        except:
            print("ERROR: File missing or does not exist")

    length = ""
    while length.isdigit():
        length = input("Enter desired length of key")
        if length.isdigit():
            if int(length) <= 1:
                length = ""
                print("ERROR: integer can not be 1 or less")
        else:
            print("ERROR: integer not entered")

    generateFiles(filePath, length)



def generateFiles(file, length):
    fileText = ""
    with open(file, "r") as testFile:
        line = testFile.readline()
        while line != '':
            fileText += line
            line = testFile.readline()
    fileKey = keyGenerator(8)

def main():
    fileText = ""
    with open("HTML File Extension - What is an .html file and how do I open it_.html", "r") as testFile:
        line = testFile.readline()
        while line != '':
            fileText += line
            line = testFile.readline()
    fileKey = keyGenerator(8)

    fileEncrypt = encrypt(fileKey, fileText)

    encryptFile = open("encrypt.html", "w")
    for j in fileEncrypt:
        try:
            encryptFile.write(j)
        except:
            print("Writing to encrypted file error: couldnt write \"" + j + "\" with ord " + str(ord(j)))
            encryptFile.write(str(j.encode("utf-8")))
    encryptFile.close()

    encryptText = ""
    with open("encrypt.html", "r") as readFile:
        line = readFile.readline()
        while line != '':
            encryptText += line
            line = readFile.readline()

    fileDecryptText = decrypt(fileKey, encryptText)

    decryptFile = open("decrypt.html", "w")
    for j in fileDecryptText:
        decryptFile.write(j)
    decryptFile.close()


main()