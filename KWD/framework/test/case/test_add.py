import unittest
from nose_ittr import ittr, IttrMultiplier


class MyTestCase(unittest.TestCase):

    __metaclass__ = IttrMultiplier

    def setUp(self):
        print "setUp!"

    def tearDown(self):
        print "tearDown!!"

    @ittr(a=[1, 2, 3, 4, 5])
    def test_add(self):
        print "test_add %d" % self.a


if __name__ == '__main__':
    import nose
    nose.main()
    # unittest.main(verbosity=2)