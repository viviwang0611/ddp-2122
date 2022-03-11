#!/usr/bin/env python
# coding: utf-8

# #  1. Write a function that will take in a string parameter and return a string in its equivalent Morse code

# In[1]:


letter_morse = {"a":".-", "b":"-.-.", "c":"-...", "d":"-..",

"e":".", "f":"..-.", "g":"--.",

"h":"....", "i":"..", "j":".---", "k":"-.-",

"l":".-..", "m":"--", "n":"-.",

"o":"---", "p":".--.", "q":"--.-",

"r":".-.", "s":"...", "t":"-",

"u":"..-", "v":"...-", "w":".--",

"x":"-..-", "y":"-.--", "z":"--..",

" ":" "}

Morse_message = ""

letters =input("Input the words that you want to turn into Morse code: \n").lower()

for letter in letters:

   if letter not in letter_morse:

     print("Couldn't find '" + letter +"'. ")

   elif letter in letters:

      Morse_message += letter_morse[letter] + ' '

print("Okay: \n" + Morse_message)


# # 3. Write a function that accepts a string and prints to screen the number of uppercase letters and lowercase letters.

# In[3]:


def case_count(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass

    print ("Uppercase : ", d["UPPER_CASE"]) 
    print ("Lowercase : ", d["LOWER_CASE"])

case_count("Hello World")

