str1 = input("enter your first string: ")
str2 = input("enter your second string: ")

if(sorted(str1) == sorted(str2)):
    print ("Anagram")
else:
    print("Not Anagram ")
