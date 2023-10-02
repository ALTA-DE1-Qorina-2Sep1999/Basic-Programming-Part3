import unittest
from main import nilai

class TestKonversiNilai(unittest.TestCase):
    def test_nilai(self):
        result = nilai(80)
        self.assertEqual(result, "Nilai A", msg="Expected 'Nilai A' for input 80")
        
if __name__ == '__main__':
    unittest.main()