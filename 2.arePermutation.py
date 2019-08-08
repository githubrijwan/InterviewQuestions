str1 =raw_input("Enter First String")
str2 = raw_input("Enter second String")


def arePermutation(str1,str2):
    matching = 0
    for i in range(0,len(str1)):
        for j in range(0,len(str2)):
            if str1[i] == str2[j]:
                matching = matching + 1

    if matching == len(str1):
        return True
    else:
        return False


print (arePermutation(str1,str2))
