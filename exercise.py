from math import floor

string = "003111"
string2 = "813372"
string3 = "17935"
string4 = "56328116"
string5 = "234f"
string6 = "asdsd"
string7 = "1104932420839423804592340923429034"


def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def luckCheck(string):
    if string == '':
        return False
    elif isInt(string):
        frontSum = 0
        backSum = 0
        bNum = -1
        for num in range(0, floor(len(string)/2)):
            frontSum += int(string[num])
            backSum += int(string[bNum])
            bNum -= 1
        # print(f"First half: {frontSum}, back half: {backSum}")
        if frontSum == backSum:
            return True
        else:
            return False
    else:
        return False


print(luckCheck(string))
print(luckCheck(string2))
print(luckCheck(string3))
print(luckCheck(string4))
print(luckCheck(string5))
print(luckCheck(string6))
print(luckCheck(string7))
