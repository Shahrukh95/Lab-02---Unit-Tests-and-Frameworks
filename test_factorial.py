import unittest
import factorial

class TestFactorial(unittest.TestCase):
    def test_fact(self):                    #Test Factorial
        s = factorial.factorial()

        answer = s.find_factorial(5)        #Test with Number 5
        self.assertEqual(answer, 120)

        answer = s.find_factorial(0)        #Test with 0
        self.assertEqual(answer, 1)

        answer = s.find_factorial(-5)       #Test with Negative Number
        self.assertEqual(answer, None)

        answer = s.find_factorial('abcd')   #Test with a String
        self.assertEqual(answer, None)

        answer = s.find_factorial(999)      #Test with the value of Maximum Recursion Limit
        self.assertEqual(answer, None)


if __name__ == '__main__':
    unittest.main()
