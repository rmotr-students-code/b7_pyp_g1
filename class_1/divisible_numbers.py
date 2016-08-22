def divisible_numbers(a_list, term):
    def is_divisible(number):
        return number % term == 0
        
    return filter(lambda x: x % term == 0, a_list)
    
    return [x for x in a_list if x % term == 0]



import unittest


class DivisibleNumbersTestCase(unittest.TestCase):
    def test_many_divisible_number(self):
        result = divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)
        expected = [9, 6, 3]
        self.assertEqual(result, expected)

    def test_empty_list(self):
        self.assertEqual(divisible_numbers([], 2), [])

    def test_no_result(self):
        self.assertEqual(divisible_numbers([2, 4, 8], 5), [])


unittest.main()