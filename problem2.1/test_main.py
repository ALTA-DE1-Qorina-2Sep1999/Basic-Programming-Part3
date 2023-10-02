import unittest
from main import faktor_bilangan

class TestFaktorBilangan(unittest.TestCase):
    def test_faktor1(self):
        result = faktor_bilangan(6)
        self.assertEqual(result, "1\n2\n3\n6", msg="Expected '1\n2\n3\n6' for input 6")
    
    def test_faktor2(self):
        result = faktor_bilangan(20)
        self.assertEqual(result, "1\n2\n4\n5\n10\n20", msg="Expected '1\n2\n4\n5\n10\n20' for input 20")
        
if __name__ == '__main__':
    unittest.main()