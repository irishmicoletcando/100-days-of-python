logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#def encrypt(inputted_text, number_of_shift):
  #cipher_text = ""
  #for letter in inputted_text:
    #position = alphabet.index(letter)
    #new_position = position + number_of_shift
    #new_letter = alphabet[new_position]
    #cipher_text += new_letter
  #print(f"The encoded text is {cipher_text}")

#def decrypt(input_text, num_of_shift):
  #cipher_text = ""
  #for letter in input_text:
    #position_decrypt = alphabet.index(letter)
    #new_position_decrypt = position_decrypt - num_of_shift
    #new_letter_decrypt = alphabet[new_position_decrypt]
    #cipher_text += new_letter_decrypt
  #print(f"The decoded text is {cipher_text}")

#if direction == "encode":
  #encrypt(inputted_text=text, number_of_shift=shift)
#elif direction == "decode":
  #decrypt(input_text=text, num_of_shift=shift)

def caesar(inputted_text, num_shift, direction_text):
  cipher_text = ""
  for letter in inputted_text:
    position = alphabet.index(letter)
    if direction_text == "encode":
      new_position = position + num_shift
      cipher_text += alphabet[new_position]
    elif direction_text == "decode":
      new_position = position - num_shift
      cipher_text += alphabet[new_position]
  print(f"The {direction_text}d text is {cipher_text}")


caesar(inputted_text=text, num_shift=shift, direction_text=direction)