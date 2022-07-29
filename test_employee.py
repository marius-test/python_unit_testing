import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    
    # this will run at the beginning of the test instance
    @classmethod
    def setUpClass(cls):
        print('setupClass\n')
    
    # this will run at the end of the test instance
    @classmethod
    def tearDownClass(cls):
        print('tearDownCLass')
    
    # this will be run before every test
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Marius', 'Briscut', 35000)
        self.emp_2 = Employee('Paul', 'Suatean', 40000)
    
    # this will be run after every test
    def tearDown(self):
        print('tearDown\n')
    
    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Marius.Briscut@gmail.com')
        self.assertEqual(self.emp_2.email, 'Paul.Suatean@gmail.com')
        
        self.emp_1.first = 'Liviu'
        self.emp_2.first = 'Emil'
        
        self.assertEqual(self.emp_1.email, 'Liviu.Briscut@gmail.com')
        self.assertEqual(self.emp_2.email, 'Emil.Suatean@gmail.com')
        
    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Marius Briscut')
        self.assertEqual(self.emp_2.fullname, 'Paul Suatean')
        
        self.emp_1.first = 'Liviu'
        self.emp_2.first = 'Emil'
        
        self.assertEqual(self.emp_1.fullname, 'Liviu Briscut')
        self.assertEqual(self.emp_2.fullname, 'Emil Suatean')
        
    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
            
        self.assertEqual(self.emp_1.pay, 36750)
        self.assertEqual(self.emp_2.pay, 42000)
            
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Briscut/May')
            self.assertEqual(schedule, 'Success')
            
            mocked_get.return_value.ok = False
            
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Suatean/June')
            self.assertEqual(schedule, 'Bad response!')


if __name__ == '__main__':
    unittest.main()
