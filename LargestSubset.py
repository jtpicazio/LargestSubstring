def get_All_Sub(s):
    subStr = ""
    temp = []
    #n = 0
    for f in range(0,len(s)+1):
        for e in range(f+len(subStr)+1,len(s)+1):
            #n += 1
            if (s[f:e] in temp) and (len(s[f:e]) > len(subStr)): subStr = s[f:e]; print(subStr)
            elif (len(s[f:e]) > len(subStr)): temp.append(s[f:e])

    #print(len(s))
    #print(n)
    #print(temp)
    return subStr

def main():
    s = "abcd"*111

    print(get_All_Sub(s))

main()