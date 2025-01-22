
#We define the function ceasar cipher
def ceasar_cipher(message,shift):
# We start by creating an empty string so that whenever the conditions are met, the character will be added to the string.  
    result=""
# We then give it conditions that are applied for each character in the message.    
    for char in message:
# If the character is lower case then we use the uni code code of the first letter of the alphabet which is 97 
# the ord function helps us convert the character to a number representing the unicode code of a specified character
# The chr function converts the number back to an alphabetical character.      
        if char.islower():
            result+=chr((ord(char)+shift -97)%26+97)
# All alphabetic characters have a different unicode code for lower and upper case
# If the character is upper case we use the unicode code of the first letter of the alphabet which is 65        
        elif char.isupper():
            result+=chr((ord(char)+ shift -65)%26+65)
        else:
            result+=char
    return result
#the function will return the result with all alphabetic characters encrypted or decrypted depending on the user's choice.
while True:
    action=input("Would you like to (E)ncrypt or (D)ecrypt a message?\n (Q) to quit: ")
    if action == 'Q':
        break
# We then prompt a user to choose to encrypt or decrypt and thereafter input a message and a shift value   
    message=input("Enter your message: ")
    shift=int(input("Enter shift value from 1-25: "))
    if action == 'E':
# When the user chooses to encrypt, the function will run as defined above    
        message=ceasar_cipher(message,shift)
        print("The encrypted message is", message)
    elif action == 'D':
# When the user chooses to decrypt, we put a - before shift because we are doing the reverse of what we designed the function to do.    
        message=ceasar_cipher(message,-shift)
        print("The decrypted message is", message)
    else:
        print("Invalid input please enter D,E,Q") 
# if the user inputs alphanumeric values, they will be returned the same exact way because that is what we included in the function.