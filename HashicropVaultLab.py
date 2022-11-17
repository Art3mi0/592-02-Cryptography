import os
import base64

def main():
    # Vault setup
    userToken = input("enter your server root token: ")
    os.environ["VAULT_ADDR"] = "http://127.0.0.1:8200"
    os.environ["VAULT_TOKEN"] = userToken
    os.system("vault secrets enable transit")
    os.system("vault write transit/keys/aesKey type=aes256-gcm96")

    # Encoding user message to base64, then encoding with vault
    userText = input("Enter message to encrypt: ")
    userText = base64.b64encode(userText.encode("utf-8"))
    encodedText = str(userText, "utf-8")
    encodeCommand = "vault write transit/encrypt/aesKey plaintext=" + encodedText
    os.system(encodeCommand)

    # Using the vault to decrypt the cipher text with error handling
    flag = True
    while flag:
            cypherText = input("Please copy and paste the ciphertext value: ")
            decodeCommand = "vault write transit/decrypt/aesKey ciphertext=" + cypherText
            check = os.system(decodeCommand)
            if check == 0:
                flag = False
            else:
                print("The input may not have been copied correctly. Make sure to include the "
                        "\"vault:v1:\" part.")

    # Turning the base64 into ascii
    decodedText = input("Please enter the decoded plaintext value: ")
    print("The decoded value is: " + base64.b64decode(decodedText).decode('utf-8'))

main()