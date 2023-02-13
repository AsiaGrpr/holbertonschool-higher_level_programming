import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_default_ID(self):
        #default ID should be Base.__nb_objects
        base = Base()
        self.assertEqual(base.id, 1)

    def test_default_new_id(self):
        base = Base()
        base2 = Base()
        self.assertEquals(base.id, 2)
        self.assertEquals(base2.id, 3)


    def test_ID(self):
        #if ID is not None, ID == value
        base = Base(89)
        self.assertEqual(base.id, 89)
