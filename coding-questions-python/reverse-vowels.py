'''
Write a function that takes a string as input and reverse only the vowels of a string.
'''
def reverseVowels(str):
    if str is None:
        return None

    cString = list(str)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    start = 0
    end = len(cString) - 1

    while start < end:
        if cString[start] in vowels and cString[end] in vowels:
            cString[start], cString[end] = cString[end], cString[start]
            start, end = start + 1, end - 1

        elif cString[start] in vowels:
            end -= 1

        elif cString[end] in vowels:
            start += 1

        else:
            start, end = start + 1, end - 1

    result = "".join(cString)
    return result

# tests
import unittest
class TestReverseVowels(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(reverseVowels("hello"), "holle")
        self.assertEqual(reverseVowels("egg"), "egg")
        self.assertEqual(reverseVowels("fry"), "fry")
        self.assertEqual(reverseVowels(""), "")
unittest.main()