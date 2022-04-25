menu={"자장면":5000,"짜장면":5000,"짬뽕":6000,"볶음밥":7000,"탕수육":15000}
menu_sum=0
while True:
    menu_select=input("메뉴를 선택하세요: ")
    if menu_select in menu:
        menu_sum=menu_sum+menu[menu_select]
        print("주문을 완료하셨으면 주문종료를 입력해주세요.")
    elif menu_select=="주문종료":
        break
    else:
        print("다시 주문해주세요. \n주문을 멈추고 싶을 경우 주문종료를 입력해주세요.")
print("총 가격은 {}원 입니다.".format(menu_sum))   
