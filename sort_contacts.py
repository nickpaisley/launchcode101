#Sort_Contacts app
#Author - Nick Paisley
#Created - 3.8.19
#Write a sort_contacts function that takes a dictionary of contacts as a 
#parameter and returns a sorted list of those contacts, where each contact is a tuple.
#The contacts dictionary that will be passed into the function has the contact name as its key, 
#and the value is a tuple containing the phone number and email for the contact.

#contacts = {name: (phone, email), name: (phone, email), etc.}

#create dictionary for contacts
contacts = {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
"Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
"Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}

def sort_contacts(contacts):
    return (sorted(contacts))

#for key in sorted(char_dict):
#             print(key, char_dict[key])

#print(contacts)
print(sort_contacts(contacts))