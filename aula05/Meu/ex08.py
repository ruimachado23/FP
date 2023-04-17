s = input("String: ")
def evenThenOdd(s):
    t = ""
    for i in s[0::2]:
        t += i
    for j in s[1::2]:
        t += j
    return t
    
def removeAdjacentDuplicates(word):
    result=""
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            result+=word[i]
    result+=word[-1]
    return result

n = input("Call a number: ")
def reapeatNumTimes(n):
    lst= []
    for i in range (1,n+1):
        for j in range(n):
            lst.append(i)
    return lst






            

