def get_initials(fullname):
    #initials = (fullname[0:1] + fullname[1:1])
    fullnames = fullname.split()
    init = ""
    for char in fullnames:
        init = init + char[0]
    result = "{}".format(init.upper())
    #print(init)
    return result

def main():
    fullname = input("What is your full name?")
    print(get_initials(fullname))


if __name__ == '__main__':
    main()