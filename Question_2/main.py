"""
Question 2: -

Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
he can remove just one character at the index in the string, and the remaining characters will occur the same
number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .


Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
an explanation for the same.


Example input 1 - s = “abc”. This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }

Example output 1- YES

Example input 2 - s “abcc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }

Example output 2 - NO
"""

from collections import Counter

def validateString(string):
        charWithCounts = Counter(string)
        frequencyCounts = Counter(charWithCounts.values())
        # print(charWithCounts)
        # print(frequencyCounts)
        # print(len(frequencyCounts))
        
        if len(frequencyCounts) == 1:
            return "YES"
        if len(frequencyCounts) > 2:
            return "No"
        
        min_freq, max_freq = sorted(frequencyCounts.keys())
        
        # print(min_freq, max_freq)
        # print(frequencyCounts[min_freq])
        
        if max_freq - min_freq == 1 and frequencyCounts[max_freq] == 1:
            return "YES, by removing one occurence of a character otherwise NO"

        if min_freq == 1 and frequencyCounts[min_freq] == 1:
            return "YES, by removing one occurence of a character Otherwise No"

        return "NO"
    


if __name__ == "__main__":
        
    a = "abc"
    b = "abcc"
    c = "aabbcc"
    d = "aabbccdc"

    print(validateString(a))
    print(validateString(b))
    print(validateString(c))
    print(validateString(d))
