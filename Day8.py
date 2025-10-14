#Caeser Cipher 

alph = [chr(i) for i in range(97, 123)]*2
print(alph)

def enc_letter(letter, k):
    for i in range(0,26):
        if alph[i] == letter:
            return alph[i+k]
        elif letter == " ":
            return " "
        
def dec_letter(letter, k):
    for i in range(0,26):
        if alph[52-i-1] == letter:
            return alph[-i-5-1]
        elif letter == " ":
            return " "
        

# print(enc_letter('b', 5))
# print(dec_letter('y', 5))
# var = 'bad'
# for i in var:
#     print(i)

# for i in range(len('bad')):
#     print('bad'[i])

def encryptor(input, size):
    encrypted = ""
    for i in input:
        encrypted += enc_letter(i, size)
    return encrypted

# print(encryptor('zebra', 5))

def decryptor(input, size):
    decrypted = ""
    for i in input:
        decrypted += dec_letter(i, size)
    return decrypted

def caeser_cipher(choice, input, size):
    if choice == 'encode':
        return(encryptor(input, size))
    elif choice == 'decode':
        return(decryptor(input, size))
    else:
        return "Invalid input"


choice = input("Type 'encode' to encrypt, 'decode' to decrypt ")
input1 = input("Type your message ")
size = int(input("Type the shift number "))

result = caeser_cipher(choice, input1, size)
print(f"Here is the encoded result: {result}")
