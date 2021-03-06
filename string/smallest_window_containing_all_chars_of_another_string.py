# Python3 program to find the smallest window containing all characters of a pattern.
# Given two strings string1 and string2, the task is to find the smallest substring in string1
# containing all characters of string2 [Asked in : Facebook, J P morgan]
no_of_chars = 128


# Function to find smallest window
# containing all characters of 'pat'
def findSubString(string, pattern):
    len1 = len(string)
    len2 = len(pattern)

    # check if string's length is less than pattern's
    # length. If yes then no such window can exist
    if len1 < len2:
        print("No such window exists")
        return ""

    hash_pat = [0] * no_of_chars
    hash_str = [0] * no_of_chars

    # store occurrence ofs characters of pattern
    for i in range(0, len2):
        hash_pat[ord(pattern[i])] += 1

    start, start_index, min_len = 0, -1, float('inf')

    # start traversing the string
    count = 0  # count of characters
    for j in range(0, len1):

        # count occurrence of characters of string
        hash_str[ord(string[j])] += 1

        # If string's char matches with pattern's char then increment count

        if hash_pat[ord(string[j])] != 0 and hash_str[ord(string[j])] <= hash_pat[ord(string[j])]:
            count += 1

        # if all the characters are matched
        if count == len2:

            # Try to minimize the window i.e.,
            # check if any character is occurring more no. of times than its occurrence in pattern,
            # if yes then remove it from starting and also remove the useless characters.
            while hash_str[ord(string[start])] > hash_pat[ord(string[start])] or hash_pat[ord(string[start])] == 0:
                if hash_str[ord(string[start])] > hash_pat[ord(string[start])]:
                    hash_str[ord(string[start])] -= 1
                start += 1

            # update window size if smalled window is found. update start_index as well
            len_window = j - start + 1
            if len_window < min_len:
                min_len = len_window
                start_index = start

            # If no window found
    if start_index == -1:
        print("No such window exists")
        return ""

    # Return substring starting from start_index and length min_len
    return string[start_index: start_index + min_len]


# Driver code
if __name__ == "__main__":
    string = "geeksforgeeks"
    pat = "ork"

    print("Smallest window is : ")
    print(findSubString(string, pat))

    string = "ADOBECODEBANC"
    pat = "ABC"

    print("Smallest window is : ")
    print(findSubString(string, pat))
