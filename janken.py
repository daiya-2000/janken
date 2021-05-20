import random

computer = ["gu", "choki", "pa"]
user = ["gu", "choki", "pa"]

while True:
    print("gu = 0:choki = 1: pa = 2")
    choose_user = int(input("choose number>"))
    choose_computer = random.randint(0, 2)
    print("user:" + user[choose_user])
    print("computer:" + computer[choose_computer])
    if user[choose_user] == computer[choose_computer]:
        print("aiko")
    elif choose_user == 0 and choose_computer == 1 or choose_user == 1 and choose_computer == 2 or choose_user == 2 and choose_computer == 0:
        print("kachi")
        break
    elif choose_user == 0 and choose_computer == 2 or choose_user == 1 and choose_computer == 0 or choose_user == 2 and choose_computer == 1:
        print("make")
        break
