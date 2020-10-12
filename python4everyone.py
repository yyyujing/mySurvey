
# split a string of sentence into words and return
# a list of words in the sequnce that the word length is decending
txt = 'but soft what light in youder window breaks'
words = txt.split() # break the string into words, sepreate by empty space
t = list()
for word in words:
    t.append((len(word),word))  # append function can only append one element per time

t.sort()  # use the build in function for list
# sort by the length (the first value in the tuples
# because this is a list of tuples, and tuples are comparable like 1-10
# so can use sort for a list of tuples
# sort() always sort the first value in the tuples

result = list()

for len, word in t:
    result.append(word)

print(result)


d = {'a':10, 'b':12, 'c': 20}
t = d.items()  # the items() function return a view object, not a list object
# to make it a list
t = list(t)
print(t) # t is a list of tuples

dic ={

}  # define an empty dictionary
dic ['we','sdf']= 'df'  # use a tuples as the key. here the bracket is left out.

print(dic)


print ( int(0.807))

class number:
    def print_number(self,number):

        while number >0:
            digit = int(number % 10)
            print(digit)
            number = int(number / 10)



test = number()
test.print_number(807)


number = (1000000000000000000000000000466/10)
print (number)



s = 'bb'
print (s[0:2])

s= "OM3100"

if "3X00" in s:
    print(True)


# this is a brute force solution and basically
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        if len(s) == 1:
            return s
        for start in range(len(s)):
            # the start of the window loop through the str

            end = len(s)
            while end > start:
                current_s = s[start:end]
                # print('start',start)
                # print("end",end)
                # print(current_s)
                if current_s == current_s[::-1]:
                    current_len = len(current_s)
                    # print(current_len)
                    if current_len >= max_len:
                        result_start = start
                        result_end = end
                        max_len = current_len
                        # print ("result_start", result_start)
                        # print("result_end",result_end)
                end = end - 1

        result_str = s[result_start:result_end]
        # print(result_str)
        return result_str


# improved version, even though also used a for and while
# use a window to control the length of substring that is being checked

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for window in range(len(s), 0, -1):
            i = 0
            while i+window <= len(s):
                ss = s[i:window+i]
                if ss == ss[::-1]:
                    return ss
                i += 1