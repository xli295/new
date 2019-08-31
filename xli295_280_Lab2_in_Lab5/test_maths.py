import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        #Arrange
        #Act
        value = maths.add(1, 2)
        
        #Assert
        self.assertEqual(3, value)

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        #Arrange
        #Act
        value = maths.fibonacci(5)
        
        #Assert
        self.assertEqual(5, value)
        
    def test_convert_base_under10(self):
        #Arrange
        #Act
        value = maths.convert_base(38, 8)
        
        #Assert
        self.assertEqual(46, int(value))
        
    def test_convert_base_over10(self):
        #Arrange
        #Act
        value = maths.convert_base(38, 12) 
        
        #Assert
        self.assertEqual(32, int(value))
        
    def test_add_optional_parameter_under10(self):
        #Arrange
        #Act
        value = maths.add(10, 30, 8)
        
        #Assert
        self.assertEqual(50, value)
        
    def test_add_optional_parameter_over10(self):
        #Arrange
        #Act
        value = maths.add(10, 30, 12) 
        
        #Assert
        self.assertEqual(34, value)
        
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
