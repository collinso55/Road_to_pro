number= int(input("please enter number to be reversed"))
def reverse_interger(number):
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1 
    reverse_str= str(number)[::-1]
    if number< 0:
        reversed_string= int('-' + str(number)[1:][::-1])
        print(reversed_string)
    else:
        print(int(reverse_str))
    if reverse_str< 'INT_MIN' or reverse_str> 'INT_MAX':
        return 0
reverse_interger(number)