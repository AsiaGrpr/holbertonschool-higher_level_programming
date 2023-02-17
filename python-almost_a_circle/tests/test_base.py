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

    def test_5(self):
        Base.to_json_string([])

    def test_6(self):
        Base.save_to_file([])

    def test_7(self):
        Base.save_to_file(None)

    def test_8(self):
        Base.to_json_string([])

    def test_9(self):
        Base.to_json_string([ { 'id': 12 }])

    def test_10(self):
        Base.from_json_string(None)

    def test_11(self):
        Base.from_json_string("[]")

    def test_12(self):
        Base.from_json_string("[]")

    def test_13(self):
        Base.from_json_string('[{ "id": 89 }]')

    def test_14(self):
        Base.from_json_string('[{ "id": 89 }]')

if __name__ == '__main__':
    unittest.main()
