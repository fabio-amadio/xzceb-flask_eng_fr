import unittest
import sys
sys.path.append('../')

from translator import english_to_french, french_to_english

class TestFrToEn(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(None), None) 
    def test2(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello") 

class TestEnToFr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(None), None)
    def test2(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") 

unittest.main()


