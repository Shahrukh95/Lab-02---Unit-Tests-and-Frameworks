import unittest
import stack

class TestStack(unittest.TestCase):
    def test_push(self):                    #Test Push
        s = stack.Stack()                   #Initiate Stack

        s.push(10)                          #Push 10
        answer = s.peek()                   #Peek and save answer to variable
        self.assertEqual(answer, 10)        #See if it Equals 10

        s.push(-5)                          #Repeat Process for -5
        answer = s.peek()
        self.assertEqual(answer, -5)

        s.push('abcde')                     #Repeat Process for 'abcde'
        answer = s.peek()
        self.assertEqual(answer, 'abcde')

    def test_pop(self):                     #Test POP
        s = stack.Stack()                   #Initialize Pop
        s.push('abcde')                     #First Push onto Stack

        answer = s.pop()                    #Pop Stack and Save it into Variable
        self.assertEqual(answer, 'abcde')   #See if the same string is returned

        self.assertFalse(s.pop())           #Stack is empty. So this should return False

    def test_isEmpty(self):                 #Check if Stack is Empty
        s = stack.Stack()                   #Initialize Stack

        self.assertTrue(s.isEmpty())    #Stack is Empty so it should be true
        s.push(10)                      #Add A Value to Stack
        self.assertFalse(s.isEmpty())   #Now it should return false becuase stack is not empty


if __name__ == '__main__':
    unittest.main()
