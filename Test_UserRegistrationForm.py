'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-01 17:10
	@Title : Unit Testing For User Registration Form 
	
'''
import unittest
import UserRegistrationForm

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



if __name__ == "__main__":
    unittest.main()
