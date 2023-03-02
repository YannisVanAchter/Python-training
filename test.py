import unittest

# SUT
from my_queue import MyQueue

class TestMyQueue(unittest.TestCase):
    
    def setUp(self):
        self.arguments = ("jkanf", "kjhajfn", 1821)
        
    def test___init__(self):
        q = MyQueue(*self.arguments, size=10)
        # example de test pour vérifier qu'une variable est bien une instance d'un objet spécifique
        self.assertIsInstance(q, MyQueue, "Mon message") 
        self.assertEqual(q.queue, self.arguments[0], "My queue is ok")
        # assert q.queue == self.arguments[1], "My queue is ok from assert"
        
        self.assertRaises(ValueError, MyQueue, *self.arguments, size=-10)
        
        with self.assertRaises(ValueError) as err:
            MyQueue(*self.arguments, size=-10)
        self.assertEqual(type(err.exception), ValueError, "My queue not raise expected error")
        
        
        

if __name__ == "__main__":
    unittest.main()