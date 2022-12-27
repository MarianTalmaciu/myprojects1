import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here  # ASCII table
uppercaseLetter1=chr(random.randint(65,90)) 
lowercaseLetter2=chr(random.randint(97,122)) 
uppercaseLetter3=chr(random.randint(65,90)) 
lowercaseLetter4=chr(random.randint(97,122)) 
uppercaseLetter5=chr(random.randint(65,90)) 
digit6=chr(random.randint(48,57)) 
punctuationSign7=chr(random.randint(32,152)) 
uppercaseLetter8=chr(random.randint(65,90)) 

#Generate password using all the characters, in random order
password = uppercaseLetter1 + lowercaseLetter2 + uppercaseLetter3 + lowercaseLetter4 + uppercaseLetter5 + digit6 + punctuationSign7 + uppercaseLetter8
password = shuffle(password)

#Ouput
print(password)