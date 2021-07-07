import unittest

def get_awkward(x: int):
    if 1>x>1000:
        return
    if x % 2 == 1:
        is_awkward = 'Awkward'
    elif x % 2 == 0 and 2<=x<=7:
        is_awkward = 'Not Awkward'
    elif x % 2 == 0 and 9<=x<=22:
        is_awkward = 'Awkward'
    elif x % 2 == 0 and x>22:
        is_awkward = 'Not Awkward'
    print(is_awkward)
    return is_awkward
    



###### UNIT TESTS ######
class TestAwkward(unittest.TestCase):
    def test_odd(self):
        test_nums = [1, 3, 5, 7, 13, 17, 19, 31, 103]
        for num in test_nums:
            self.assertEqual(get_awkward(num), 'Awkward')

    def test_first_even(self):
        test_nums = [2, 4, 6]
        for num in test_nums:
            self.assertEqual(get_awkward(num), 'Not Awkward')

    def test_second_even(self):
        test_nums = [10, 12, 14, 16, 18, 20, 22]
        for num in test_nums:
            self.assertEqual(get_awkward(num), 'Awkward')

    def test_third_even(self):
        test_nums = [24, 40, 80, 64, 28, 54, 44]
        for num in test_nums:
            self.assertEqual(get_awkward(num), 'Not Awkward')