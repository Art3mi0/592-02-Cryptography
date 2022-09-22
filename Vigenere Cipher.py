import random

def keyGenerator(length):
    key = ""
    while len(key) != length:
        key += chr(random.randint(65, 90))
    return key

def encrypt(key, x):
    cipher = ""
    message = x
    # min = 100
    for i in range(len(message)):
        temp = ord(message[i])+ ord(key[i])- 64
        if temp > 127 & temp < 200:
            temp -= 127
        if temp > 200:
            cipher += message[i]
        else:
            cipher += chr(temp)
    print(min)
    return cipher

def decrypt(key, cipher):
    message = ""
    for i in range(len(key)):
        temp = ord(cipher[i])- ord(key[i])+ 64
        if temp <= 0:
            temp += 127
        if temp > 200:
            message += cipher[i]
        else:
            message += chr(temp)
    return message

def main():
    print(ord("€"))
    print(chr(8364))
    fileText = ""
    with open("HTML File Extension - What is an .html file and how do I open it_.html", "r") as testFile:
        line = testFile.readline()
        while line != '':
            fileText += line
            line = testFile.readline()
    fileKey = keyGenerator(len(fileText))
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