class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        all_substring = get_all_substrings(s)
        for substring in all_substring:
            if check_repeat_in_string(substring):
                if len(substring) > result:
                    result = len(substring)
        return result

def get_all_substrings(input_string):
        length = len(input_string)
        return [input_string[i:j + 1] for i in range(0, length) for j in range(i, length)]

def check_repeat_in_string(input_string):
        dic = {}
        for char in input_string:
            if char not in dic:
                dic[char] = 1
            else:
                return False
        return True

# the other two functions have to not be inside the class
# need to investigate why
# to make the function able to be inside the class, need to be like:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        all_substring = self.get_all_substrings(s)
        for substring in all_substring:
            if self.check_repeat_in_string(substring):
                if len(substring) > result:
                    result = len(substring)
        return result

    def get_all_substrings(self, input_string):
        length = len(input_string)
        return [input_string[i:j + 1] for i in range(0, length) for j in range(i, length)]

    def check_repeat_in_string(self, input_string):
        dic = {}
        for char in input_string:
            if char not in dic:
                dic[char] = 1
            else:
                return False
        return True

#have to use self to call the function defined within the class



def check_repeat_in_string(input_string):
    dic = {}
    for char in input_string:
        if char not in dic:
            dic[char] = 1
        else:
            return True
    return False


s = 'sdhfff'
result = check_repeat_in_string(s)

print(result)

s2 ='asdfgh'

result2 = check_repeat_in_string(s2)

print(result2)



# dynamic programming for finding the longest 