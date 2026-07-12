#Creating a password generator 
import random 
import string

string_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_num = '0123456789'
string_special = '!@#$%^&*()_+'

def user_input():
    length = int(input("Enter length required:"))
    use_special = input("Include special characters?(yes/no):").lower() == 'yes'
    use_num = input("Include numbers?(yes/no): ").lower() == 'yes'
    return (length,use_special,use_num)


def generate_pass(length,use_special,use_num):
    password = ''
    if use_special is True and use_num is True :
        for _ in range(length-1):
            password += random.choice(string_char)
    else :
        for _ in range(length):
            password += random.choice(string_char)
    if use_special is True :
        password += random.choice(string_special)
    if use_num is True :
        password += random.choice(string_num)
    return password


if __name__ == '__main__' :
    length,use_special,use_num = user_input()
    generated_pass =generate_pass(length,use_special,use_num)
    print("Password is :"+ generated_pass)
