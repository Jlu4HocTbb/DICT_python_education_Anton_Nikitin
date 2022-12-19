import random

integer = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
intinput = int(input("Enter the number of friends joining (including you):\n>"))


#проверка ввода

if intinput < 1:
    print("No one is joining for the party")

else:
    friendslov = {}


#список: кол-во и имя обьектов

    print("Enter the name of every friend (including you), each on a new line:")

    for i in range(0, intinput):
        friendslov[input("")] = 0

    print(friendslov)


# вычисление суммы на каждого

    print("Enter the total amount")
    userinput = float(input(">"))


# выбор лаки

    print("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    user = input(">")

#Yes
    if user == "Yes":

        random1 = random.choice(list([*friendslov]))

        for i in friendslov:
            friendslov[i] = round(userinput / (len(friendslov) - 1), 2)

        friendslov[random1] = 0

        print(random1 + " is the lucky one!")
        print(friendslov)

#No
    else:
        print("No one is going to be lucky\n")

        for i in friendslov:
            friendslov[i] = round(userinput / len(friendslov), 2)

        print(friendslov)