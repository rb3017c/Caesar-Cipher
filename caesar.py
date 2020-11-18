#!/usr/bin/env python3

#Script to decode file encrpted with Caesar Cipher
#Code works with file: somefile.txt

#needed for string.ascii and sys.argv[]
import string
import sys

#assigns the letters of the alphabet to variable
alphabet = string.ascii_letters 
decrypted = ""


#assigns the second field to a variable
file_name= sys.argv[1]

with open(file_name, 'r') as f:
    cipher_text= f.read()

key = 0

#parse each line in file
for lines in cipher_text:


    if lines != "\n":

#parse items in each line
        for c in lines: 

            if c in alphabet:
                if c == c.upper():
                    position = string.ascii_uppercase.find(c)
                    shift = (position + key) % 26
                    new_character = string.ascii_uppercase[shift]
                    decrypted += new_character
                else:
                    position = string.ascii_lowercase.find(c)  
                    shift = (position + key) % 26
                    new_character = alphabet[shift]
                    decrypted += new_character

            else:
                decrypted += c
                key -= 1
    else:
        decrypted += "\n"
        key = 0

print(decrypted)
