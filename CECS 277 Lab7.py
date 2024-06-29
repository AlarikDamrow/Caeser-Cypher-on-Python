# Group 6
# Alarik Damrow , Anthony Hernandez-Torres
# October 5 2022
import cypher
import caesar_cipher
import check_input
def main ():
    '''This is how the program will ask user for values and based on those
    choices it will run certain encryption and decryption and create a cypher
    or ceasar cypher classes'''
    choice1 = 0
    choice2 = 0
    print("Secret Decoder Ring:")
    print("1. Encrypt")
    print("2. Decrypt")
    choice1 = check_input.get_int_range(0,2)
    if choice1 == 1:
        print("Enter encryption type:")
        print("1. Atbash")
        print("2. Caesar")
        choice2 = check_input.get_int_range(0,2)
        if choice2 == 1:
            file = open("message.txt", "w")
            print("Enter message: ",end="")
            idea = input()
            c1 = cypher.Cypher()
            enidea = c1.encrypt_message(idea)
            file.write(enidea)
            print ("Encrypted message saved to “message.txt”.")
        else:
            file = open("message.txt", "w")
            print("Enter message: ",end="")
            idea = input()
            print("Enter shift value:", end ="")
            shift = int(check_input.get_int_range(0,25))
            c1 = caesar_cipher.CasesarCipher(shift)
            enidea = c1.encrypt_message(idea)
            file.write(enidea)
            print ("Encrypted message saved to “message.txt”.")
    else:
        print("Enter decryption type:")
        print("1. Atbash")
        print("2. Caesar")
        choice2 = check_input.get_int_range(0,2)
        if choice2 == 1:
            file = open("message.txt", "r")
            idea = file.read()
            print("Encrypted message written to file: ",end="")
            print(idea)
            c1 = cypher.Cypher()
            deidea = c1.decrypt_message(idea)
            print("Decrypted message: ",end="")
            print (deidea)
        else:
            file = open("message.txt", "r")
            idea = file.read()
            print("Encrypted message written to file: ",end="")
            print(idea)
            print("Enter shift value:", end ="")
            shift = int(check_input.get_int_range(0,25))
            c1 = caesar_cipher.CasesarCipher(shift)
            deidea = c1.decrypt_message(idea)
            print("Decrypted message: ",end="")
            print (deidea)
main()
