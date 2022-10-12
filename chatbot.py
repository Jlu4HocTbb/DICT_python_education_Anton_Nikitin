# 1 stage

print("Hello! My name is DICT_Bot")
print("I was created in 2022")



# 2 stage

name = input("Please, remind me your name.\n")

print("What a great name you have, "+name +"!")



# 3 stage

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

remainder3 = int(input(""))
remainder5 = int(input(""))
remainder7 = int(input(""))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")



# 4 stage

print("Now I will prove to you that I can count to any number you want.")

n = int(input(""))
i = 1

while i<=n:
    print(str(i) + "!")
    i=i+1



# 5 stage
#Test

print("Let's test your programming knowledge.")
print("how many arithmetic operators are there?\n1. 7\n2. 8\n3. 4")

while True:
    user_input = input()
    if user_input == "7":
        print("Completed, have a nice day!")
        print("Congratulations, have a nice day!")
        break
    print("Please, try again.")


























































