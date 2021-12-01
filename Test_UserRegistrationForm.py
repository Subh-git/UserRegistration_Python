'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-01 17:10
	@Title : Unit Testing For User Registration Form 
	
'''
import unittest
import UserRegistrationForm
import EmailSamples

class Test_UserRegistration(unittest.TestCase):

    def test_first_name(self):
        '''
        This method is to test the validity of first name. It checks whether the called function returns valid or invalid.
        '''
        self.assertEqual(UserRegistrationForm.first_name('Subhadeep'),'Valid')
        self.assertEqual(UserRegistrationForm.first_name('subhadeep'),'Invalid')
        self.assertEqual(UserRegistrationForm.first_name('Rahul'),'Valid')
        self.assertEqual(UserRegistrationForm.first_name('Ro'),'Invalid')
        self.assertEqual(UserRegistrationForm.first_name('Subhadeep Bhatta'),'Invalid')

    def test_last_name(self):
        '''
        This method is to test the validity of last name. It checks whether the called function returns valid or invalid.
        '''
        self.assertEqual(UserRegistrationForm.last_name("Bhattacharjee"),"Valid")
        self.assertEqual(UserRegistrationForm.last_name("Gaikwad"),"Valid")
        self.assertEqual(UserRegistrationForm.last_name("Bh"),"Invalid")
        self.assertEqual(UserRegistrationForm.last_name("bhattacharjee"),"Invalid")

    def test_email(self):
        '''
        This method is to test the validity of the email address. It checks whether the called function returns valid or invalid.
        '''
        self.assertEqual(UserRegistrationForm.email_name("Subhadip@gmail.com"),"Valid")
        self.assertEqual(UserRegistrationForm.email_name("subhadeep.com"),"Invalid")
        self.assertEqual(UserRegistrationForm.email_name("Subhadeep@gmail"),"Invalid")

    def test_mobile(self):
        '''
        This method is to test the validity of the mobile number. It checks whether the called function returns valid or invalid.
        '''
        self.assertEqual(UserRegistrationForm.mobile_number("91 8529637413"),"Valid")
        self.assertEqual(UserRegistrationForm.mobile_number("8529637413"),"Invalid")
        self.assertEqual(UserRegistrationForm.mobile_number("910 8529637413"),"Valid")

    def test_password(self):
        '''
        This method is to test the validity of the password. It checks whether the called function returns valid or invalid.
        '''
        self.assertEqual(UserRegistrationForm.password("Abchou123@"),"Valid")
        self.assertEqual(UserRegistrationForm.password("shjkioertp"),"Invalid")
        self.assertEqual(UserRegistrationForm.password("aQo@334"),"Invalid")


    #the below tests are for testing all the valid and invalid testing mails.  
    def test_all_valid_emails(self):
        '''
        This method is to test the validity of all the valid email samples. 
        It checks whether the called function returns valid or invalid.
        '''
        string = "Valid"
        for i in EmailSamples.ValidEmails:
            self.assertEqual(UserRegistrationForm.email_name(i),string)

    def test_all_invalid_emails(self):
        '''
        This method is to test the validity of all the invalid email samples. 
        It checks whether the called function returns valid or invalid.
        '''
        string = "Invalid"
        for i in EmailSamples.InValidEmails:
            self.assertEqual(UserRegistrationForm.email_name(i),string)



if __name__ == "__main__":
    unittest.main()
