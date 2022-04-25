import random
number=random.randint(1,100)
print("1부터 100사이의 숫자를 맞추시오")
while True:
    guess=int(input("숫자를 입력하시오: "))
    if guess < number:
        print("낮음!")
    elif guess> number:
        print("높음!")
    else:
        break
print("축하합니다.")
