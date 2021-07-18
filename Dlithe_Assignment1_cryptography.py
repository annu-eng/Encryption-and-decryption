
# Encrypting function.


def encrypter (data, key, mode):
    new_data = ''
    alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'

    new_index = int
    for c in data:
        index = alphabet.find(c)

        if index == -1:
            new_data += c
        else:
                new_index = index + key if mode == 1 else index - key
                new_index %= len(alphabet)
                new_data += alphabet[new_index:new_index + 1]
    return new_data

# Pseudo privacy function.


def spacer():
    for i in range(1000):
        print(" ")


print("caeser welcomes you....")

# Main program.

while(1):
    f = input(print('encryption(E) or decrypton(D)?'))
    l = f.upper()
    if l == 'E':
        data = input("enter the data to be encrypted")
        key=int(input("enter the magic number"))
        ciphered = encrypter(data, key, 1)
        print('your encrypted data is', ciphered)
        input('press enter once done')
        spacer()
    elif l == 'D':
        bata = input("enter the data to be dencrypted")
        key = int(input("enter the magic number"))
        plain = encrypter(bata, key, 0)
        print('your decrypted data is', plain)
        input('press enter once done')
        spacer()
    else:
        print('''
        for encryption, press 'E'
        for decryption, press 'D' 
              ''')