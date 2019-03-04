#Counting_Characters app
#author - Nick Paisley
#created - 3.4.19

#Write a program that calculates the number of times each character occurs in a string and prints these stats to the console.
#Here’s a test string, for your convenience

test_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."

def char_times(test_string): 
    times = ""
    for char in test_string:
        times = times + char(0)