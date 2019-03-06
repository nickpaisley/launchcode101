#Counting_Characters app
#author - Nick Paisley
#created - 3.4.19
#finished - 3.6.19

#Write a program that calculates the number of times each character occurs in a string and prints these stats to the console.

#create test string
test_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."

#dictionary creation
char_dict = {}

#function to count all characters. 
def char_count(string):
    for char in test_string:
        char_dict[char] = test_string.count(char) 
   
#call char_count function to populate dictionary with string.
char_count(test_string)

#print and sort dictionary
for key in sorted(char_dict):
             print(key, char_dict[key])