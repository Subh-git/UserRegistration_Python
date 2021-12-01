'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-01 17:00
	@Title : User Registration Form
	
'''
import re


def first_name(string):
    '''
    Description:
        This method is used to validate the first name entered.
    Parameter:
        This takes a string as parameter.
    Return:
        This returns whether the string is Valid or Invalid.
    '''
    reg = "^[A-Z]{1}[a-zA-Z]{2,}$"
    
    if (re.match(reg,string)):
        return "Valid"
    else:
        return "Invalid"


def last_name(string):
    '''
    Description:
        This method is used to validate the last name entered.
    Parameter:
        This takes a string as parameter.
    Return:
        This returns whether the string is Valid or Invalid.
    '''
    reg = "^[A-Z]{1}[a-zA-Z]{2,}$"
    
    if (re.match(reg,string)):
        return "Valid"
    else:
        return "Invalid"
