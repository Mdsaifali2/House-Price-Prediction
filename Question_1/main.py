"""
Question 1: -

Write a program that takes a string as input, and counts the frequency of each word in the string, there might
be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
highest-frequency word.

Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
an explanation for the same.

    Example input - string = “write write write all the number from from from 1 to 100”
    Example output - 5

    Explanation - From the given string we can note that the most frequent words are “write” and “from” and
    the maximum value of both the values is “write” and its corresponding length is 5
"""

from collections import Counter

def highest_frequency_word_length(text):
    
    try : 
        text = text.split()
        wordWithCount = Counter(text)
        
        frequecy =  max(wordWithCount.values())
        
        highFrequecyWord = list()
        for word, count in wordWithCount.items():
            if count==frequecy:
                highFrequecyWord.append(word)
        
        if len(highFrequecyWord)>1:
            word = highFrequecyWord[0]
            Explaination = f"From the given string we can note that the most frequent words are : {', '.join(highFrequecyWord)} and the maximum value of both the values is {highFrequecyWord[0]} and its corresponding length is : {len(highFrequecyWord[0])}"
        else:
            Explaination = f"From the given string we can note that the most frequent words are : {str(highFrequecyWord)} and length is : {len(highFrequecyWord[0])}"
            
        return word, Explaination
    
    except Exception as e:
        print(f"please enter a valid string")


if __name__ == "__main__":
    string = "From the given string we can note that the most frequent words are :"
    result, explaination = highest_frequency_word_length(string)
    print(explaination)
    print(f"Length of {result} : {len(result)}")