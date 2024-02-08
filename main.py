'''
char-check-lab
Character Check Lab  
You may work with others on this lab.  

The check_character() function takes in two parameters, a string and an index. Fix the function so that it returns the type of the character at that index in the string. The type should be a letter, digit, whitespace, or unknown.  

For example:  
check_character('happy birthday', 2) should return "letter"  
check_character('happy birthday', 5) should return "whitespace"  
check_character('happy birthday 2 you', 15) should return "digit"  
check_character('happy birthday!', 14) should return "unknown"
yay
'''

def check_character(word, index):
   i = word[index]
   if i.isalpha():
       return("letter")
   elif i.isspace():
      return("whitespace")
   elif i.isdigit():
      return("digit")
   else:
      return("unknown")
   


if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))