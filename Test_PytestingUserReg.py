'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-02 09:30
	@Title : PyTest Testing For User Registration Form 
	
'''
import pytest
import EmailSamples
import UserRegistrationForm


def test_first_name():
    '''
    This is for doing pytest of the first name method.
    '''
    assert UserRegistrationForm.first_name("Subhadeep")=='Valid'
    assert UserRegistrationForm.first_name("subhadeep")=='Invalid'
    assert UserRegistrationForm.first_name("Su")=='Invalid'

def test_last_name():
    '''
    This is for doing pytest of the last name method.
    '''
    assert UserRegistrationForm.last_name("Bhatta")=='Valid'
    assert UserRegistrationForm.last_name("ganguly")=='Invalid'
    assert UserRegistrationForm.last_name("Bu")=='Invalid'

def test_valid_email_samples():
    '''
    This test tests all the samples which should be valid.
    '''
    string = 'Valid'
    for element in EmailSamples.ValidEmails:
        assert UserRegistrationForm.email_name(element)==string

def test_Invalid_email_samples():
    '''
    This test tests all the samples which should be invalid.
    '''
    string = 'Invalid'
    for element in EmailSamples.InValidEmails :
        assert UserRegistrationForm.email_name(element)==string

def test_mobile_number():
    '''
    This test is for testing the mobile number.
    '''
    assert UserRegistrationForm.mobile_number("91 7894561230")=="Valid"
    assert UserRegistrationForm.mobile_number("012 9895651234")=="Valid"
    assert UserRegistrationForm.mobile_number("258959") == "Invalid"

def test_password():
    '''
    This test is for checking the password.
    '''
    assert UserRegistrationForm.password("$3234AdcasSFD")=="Valid"
    assert UserRegistrationForm.password("12345678sd")=="Invalid"

