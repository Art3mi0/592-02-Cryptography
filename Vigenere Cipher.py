import random



def keyGenerator(length):
    key = ""
    while len(key) != length:
        key += chr(random.randint(65, 90))
    return key

def encrypt(key, x):
    cipher = ""
    message = x
    min = 100
    for i in range(len(message)):
        temp = ord(message[i])+ ord(key[i])- 64
        if min < ord(message[i]):
            min = ord(message[i])
            # print("Character \'" + message[i] + "\' has an ord of " + str(ord(message[i])))
        if temp > 127 & temp < 200:
            temp -= 127
        cipher += chr(temp)
    print(min)
    return cipher

def decrypt(key, cipher):
    message = ""
    for i in range(len(key)):
        temp = ord(cipher[i])- ord(key[i])+ 64
        try:
            message += chr(temp)
        except:
            # print("DECRYPT ERROR: " + cipher[i] + " with ord " + str(ord(cipher[i])) + " is being subtracted by " + str(temp))
            if temp <= 0:
                temp += 127
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
        # print(j)
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
    fileDecryptText = decrypt(fileKey, fileEncrypt)
    decryptFile = open("decrypt.html", "w")
    for j in fileDecryptText:
        # print(j)
        try:
            decryptFile.write(j)
        except:
            print(j)
            decryptFile.write(j.encode("utf-8"))
    decryptFile.close()

main()