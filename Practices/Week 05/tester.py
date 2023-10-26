import unittest
import pandas as pd
import employee
import student
class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("My Test on employee test started \n")

    @classmethod
    def tearDownClass(cls):
        print("MyTest test on employee ended \n")
        
    def setUp(self):
        print("setUp")
        self.employee_df = pd.read_csv('sample_employees.csv')
        self.salary = self.employee_df.salary

    def tearDown(self):
        print("tearDown \n")
        
    # Creating the method to test add
    def test_lower_name(self):
        print('testing get_fullname function...')
        # Saving the add function's result
        result = employee.get_fullname('Bob', 'Marley')
        # assertEqual's 1st argument is the result and 2nd argument is the expected result
        self.assertEqual(result, 'bob marley')
        
    def test_average_salary(self):
        print('testing get_average function...')
        #Saving get_average function's result
        result = employee.get_average(self.salary)
        self.assertEqual(result, self.salary.mean())
        
    
class TestStudent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("My Test on student started \n")

    @classmethod
    def tearDownClass(cls):
        print("My Test on student ended \n")

    def tearDown(self):
        print("tearDown \n")
        
    def setUp(self):
        print("setUp")
        self.students_df = pd.read_csv('sample_students.csv')
        self.grade = self.students_df.grade
        
    def test_max_grade(self):
        print('testing get_max_grade...')
        #Saving get_average function's result
        result = student.get_max_grade(self.grade)
        self.assertEqual(result, self.grade.max())
    
    def test_min_grade(self):
        print('testing get_min_grade...')
        #Saving get_average function's result
        result = student.get_min_grade(self.grade)
        self.assertEqual(result, self.grade.min())
        
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)