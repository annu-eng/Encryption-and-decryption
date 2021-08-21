#Program to encrypt or decrypt input data based on caeser cipher algorithm.

def endecrypter (data, key, mode):          #function declaration
    new_data = ''                           #string declaration to store our encrypted/decrypted data.
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
      
    new_index = int
    for c in data:
        index = alphabet.find(c)     #index of the character in the string alphabet is returned.           

        if index == -1:              #if character is not present in the string alphabet then simply append it to the output string
            new_data += c
        else:
                new_index = index + key if mode == 1 else index - key             #if mode=1 then encryption else decryption
                new_index %= len(alphabet) 
                ''''          
                  assuming index is 5 , 5%52=5 at the same time if index is 56
                  which i greater than 52(length of our alphabet string) 
                  then 56%52=4(starts from beginning of string).
                  for decryption if index is 0 then for a key =4, 0-4=-4 then -4%52=48   
                '''                 
                new_data += alphabet[new_index]                  #appending characters.
    return new_data

# Pseudo privacy function.


def spacer():
    input('press enter once done ')
    for i in range(1000):
        print(" ")


print("caeser welcomes you....")

#########    Main program     ########

while(1):
    f = input('encryption(E) or decrypton(D)? ')
    l = f.upper()
    if l == 'E':
        data = input("enter the data to be encrypted ")
        key=int(input("enter the magic number "))           # input type conversion
        ciphered = endecrypter(data, key, 1)               #function call
        print('your encrypted data is ', ciphered)
        spacer()
    elif l == 'D':
        bata = input("enter the data to be dencrypted ") 
        key = int(input("enter the magic number "))           # input type conversion
        plain = endecrypter(bata, key, 0)                    #function call
        print('your decrypted data is ', plain)
        spacer()
    else:
        j=str(input( '''
        for encryption, press 'E'
        for decryption, press 'D' 
        enter 'X' to end the program 
              '''))
        if j=='X' or 'x':
            break
