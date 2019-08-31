import unittest
from logger import Logger


class Target:
    def __init__(self, text=None):
        self.__text = text
    
    def set_text(self, text):
        self.__text = text
    
    def get_text(self):
        return self.__text
    
class LoggerTest(unittest.TestCase):
    def test_info(self):
        #Arrange
        t = Target()
        log = Logger(t.set_text)
    
        #Act
        log.info("msg1")
    
        #Assert
        self.assertEqual("[INFO] msg1", t.get_text())
    
    def test_error(self):
        #Arrange
        t = Target()
        log = Logger(t.set_text)
    
        #Act
        log.error("msg2")
    
        #Assert
        self.assertEqual("[WARNING] msg2", t.get_text())
    