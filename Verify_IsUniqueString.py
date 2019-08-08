st = raw_input ("Enter String")

def isUniqueChars(st):
    for i in range(0,len(st)):
        for j in range(i+1,len(st)):
            if st[i] == st[j]:
                return False

    return True

print (isUniqueChars(st))
