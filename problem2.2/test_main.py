import unittest
from main import faktor_bilangan

class TestFaktorBilangan(unittest.TestCase):
    def test_faktor1(self):
        result = faktor_bilangan(6)
        self.assertEqual(result, "6\n3\n2\n1", msg="Expected '6\n3\n2\n1' for input 6")
    
    def test_faktor2(self):
        result = faktor_bilangan(20)
        self.assertEqual(result, "20\n10\n5\n4\n2\n1", msg="Expected '20\n10\n5\n4\n2\n1' for input 20")
        
if __name__ == '__main__':
    unittest.main()