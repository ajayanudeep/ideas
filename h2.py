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