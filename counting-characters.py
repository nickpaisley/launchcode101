#Counting_Characters app
#author - Nick Paisley
#created - 3.4.19

#Write a program that calculates the number of times each character occurs in a string and prints these stats to the console.
#Here’s a test string, for your conveniencepoppdef

test_string = "cba"


#def char_add(test_string): 
char_dict = {}
for char in test_string:
    char_dict[char] = test_string.count(char) 
    
    
    
for key in (char_dict):
    print(key, char_dict[key]) 
    
    

#print(char_add(test_string))
#for values in (char_dict):
 #   print(values)
#for keys in (char_dict):
#    print(keys)    