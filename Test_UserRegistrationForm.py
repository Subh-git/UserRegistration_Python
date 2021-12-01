'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-01 17:10
	@Title : Unit Testing For User Registration Form 
	
'''
import unittest
import UserRegistrationForm

class Test_UserRegistration(unittest.TestCase):

    def test_first_name(self):
        self.assertEqual(UserRegistrationForm.first_name('Subhadeep'),'Valid')
        self.assertEqual(UserRegistrationForm.first_name('subhadeep'),'Invalid')
        self.assertEqual(UserRegistrationForm.first_name('Rahul'),'Valid')
        self.assertEqual(UserRegistrationForm.first_name('Ro'),'Invalid')
        self.assertEqual(UserRegistrationForm.first_name('Subhadeep Bhatta'),'Invalid')

    def test_last_name(self):
        self.assertEqual(UserRegistrationForm.last_name("Bhattacharjee"),"Valid")
        self.assertEqual(UserRegistrationForm.last_name("Gaikwad"),"Valid")
        self.assertEqual(UserRegistrationForm.last_name("Bh"),"Invalid")
        self.assertEqual(UserRegistrationForm.last_name("bhattacharjee"),"Invalid")



if __name__ == "__main__":
    unittest.main()
