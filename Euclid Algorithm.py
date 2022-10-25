"""
Author  - Temo Meza
Course  - CSC-592-02
Date    - 10/25/2022
Purpose - Assignment 4
"""

def euclid(m, n, lst, count):
    x = 0
    y = 0
    table = lst
    if n > m:
        x = n
        y = m
    else:
        x = m
        y = n
    r = x % y
    q = x // y

    table.append(count)
    table.append(q)
    table.append(x)
    table.append(y)
    table.append(r)

    if r == 0:
        track = -5
        print("%2s| %8s %8s %8s %8s" % ("i", "q", "m", "n", "r"))
        print("-"*39)
        for i in range(len(table)):
            if (i % 5) == 0:
                track += 5
                print("%2d| %8d %8d %8d %8d" % (table[0 +
                track], table[1 + track], table[2 +
                track], table[3 + track], table[4 + track]))
        print("%2d| %8s %8d %8d %8s \n" % (count + 1, " ", y, 0, "STOP"))
        return y
    else:
        return euclid(y, r, table, count + 1)

def main():
    mainFlag = True
    while mainFlag:
        flag = True
        while flag:
            try:
                test1 = input("Enter a number: ")
                test1 = int(test1)
                flag = False
            except:
                print("Number not entered. Try again")

        flag = True
        while flag:
            try:
                test2 = input("Enter a number: ")
                test2 = int(test2)
                flag = False
            except:
                print("Number not entered. Try again")

        print()
        print("the gcd of", test1, "and", test2,  "is:", euclid(test1, test2, [], 0), "\n")

        innerLoopFlag = True
        while innerLoopFlag:
            check = input("Enter 1 to test another pair of values or 0 to exit: ")
            if check == "0":
                mainFlag = False
                innerLoopFlag = False
            elif check == "1":
                innerLoopFlag = False
            else:
                print("Neither 0 or 1 was entered.")

main()