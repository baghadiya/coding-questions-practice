'''
LC (prem): https://leetcode.com/problems/reverse-words-in-a-string-ii/
Given an input string , reverse the string word by word. 
Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Note: 
A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.

Follow up: Could you do it in-place without allocating extra space?
'''

def reverseWords(self, li):
        # reverse the whole string
        self.reverse_str(li, 0, len(li) - 1)
    
        # reverse each word
        # maintain a start pointer, whenever you encounter a space, reverse the string from start to space
        # update start pointer
        start = 0
        index = 0
        while index < len(li):
            if li[index] == " ":
                self.reverse_str(li, start, index - 1)
                start = index + 1
            index += 1
        
        # reverse the last word
        self.reverse_str(li, start, len(li) - 1)
        
    
def reverse_str(self, string, start, end):
        # pointer to the first and last char of string
        # swap, and move inward, and stop when they meet
        while start < end:
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1
            
# all leetcode tests pass, as of 3rd Oct 2019
