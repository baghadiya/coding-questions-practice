'''
Write a function that compares a binary and a hexadecimal and returns true if they are equal.
Complexity analysis: O(n+m) time and O(1) space complexity
'''

def check_num_equality(bin, hex):
    return convert_from_base(bin[2:], 2) == convert_from_base(hex[2:], 16)

def convert_from_base(num, base):
    hex_dictionary = {'a': "10", 'b': "11", 'c': "12", 'd': "13", 'e': "14", 'f': "15"}
    result = 0
    len_of_num = len(num)
    for i in range(len_of_num):
        coef = num[len_of_num-1-i]
        if coef in hex_dictionary:
            coef = hex_dictionary[coef]
        result += (int(coef)*(base**i))
    return result

# tests
import unittest
class TestCheckNumEquality(unittest.TestCase):

    def test_addition(self):
        self.assertTrue(check_num_equality(bin(47), hex(47)))
        self.assertFalse(check_num_equality(bin(20), hex(15)))
        self.assertTrue(check_num_equality(bin(11), hex(11)))
        self.assertFalse(check_num_equality(bin(0), hex(10)))
        self.assertFalse(check_num_equality(bin(10), hex(0)))
        self.assertTrue(check_num_equality(bin(0), hex(0)))

unittest.main()
