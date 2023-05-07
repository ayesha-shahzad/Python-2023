str = input("provide string to check length: ")

print (len(str))

str = input("provide string to print 3 times: ")

print (str *3)

str1 = input("Enter 1st string to compare: ")
str2 = input("Enter 2nd string to compare: ")

print (str1==str2)

str = input("provide string to find longest word: ")

list = str.split()

longest_string = ''

for item in list:
    if (len(item) > len(longest_string)):
        longest_string = item

print(longest_string, '-', len(longest_string))

str = input("provide string to replace bad with good and remove not: ")

print(str.replace('bad', 'good').replace('not', ''))
