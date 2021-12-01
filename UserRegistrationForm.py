'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-01 17:05
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


def email_name(string):
    '''
    Description:
        This method is used to validate the email entered.
    Parameter:
        This takes a string as parameter.
    Return:
        This returns whether the string is Valid or Invalid.
    '''
    reg = "^[a-zA-Z0-9]+[+-._]?[a-zA-Z0-9]*[+-._]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[.]{1}[a-zA-Z]{2,3}[.]?[a-zA-Z]{0,3}$"

    if (re.match(reg,string)):
        return "Valid"
    else:
        return "Invalid"

def mobile_number(string):
    '''
    Description:
        This method is used to validate the mobile number entered.
    Parameter:
        This takes a string as parameter.
    Return:
        This returns whether the string is Valid or Invalid.
    '''
    reg = "^([0-9]{2}[ ][0-9]{10})|([0-9]{3}[ ][0-9]{10})$"

    if (re.match(reg,string)):
        return "Valid"
    else:
        return "Invalid"

def password(string):
    '''
    Description:
        This method is used to validate the password entered.
    Parameter:
        This takes a string as parameter.
    Return:
        This returns whether the string is Valid or Invalid.
    '''
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^a-zA-Z0-9]).{8,}$"

    if (re.match(reg,string)):
        return "Valid"
    else:
        return "Invalid"
