import sys
from ast import literal_eval

def get_type(num):
    try:
        return type(literal_eval(num))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str

def calc(num):
    if num%2 == 0:
        return True
    elif num == 0:
        return True
    else:
        return False
    
    

def assign(val):
    if val == True:
        return "Even"
    if val == False:
        return "Odd"
    
    
while True:
    num = input("please input number: ")
    data_type = (get_type(num))
    if data_type == int or data_type == float:
        num = int(num)
        val = calc(num)
        final = assign(val)
        print(final)

        