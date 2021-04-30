# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to
# uppercase letters and vice versa.
# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
# Input Format
# A single line containing a string .
# Constraints
# Output Format
# Print the modified string .
# Sample Input 0
# HackerRank.com presents "Pythonist 2".
# Sample Output 0
# hACKERrANK.COM PRESENTS "pYTHONIST 2".
def swap_case(s):
    new = ""
    for i in range(len(s)):
        if s[i].isupper():
            new += s[i].lower()
        elif s[i].islower():
            new += s[i].upper()
        else:
            new += s[i]
    return new

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result