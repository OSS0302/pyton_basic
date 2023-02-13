cash=int(input("현질금액할 금액을 입력해주세요"))
while True:
    print("[메뉴을 선택해주세요]")
    game_menu = (int(input("1.게임 시작 2.랭킹보기 3.캐쉬금액 확인하기  4. 게임종료>>>")))
    if game_menu== 1:
        print("->게임을 시작합니다.")
    elif game_menu ==2:
        print("실시간 랭킹")
    elif game_menu == 3:
        print(f"₩{cash}")  
    elif game_menu ==4:
        break
        print("게임을 종료합니다.")  
    else:
        print("다시입력해주세요")
       
        
