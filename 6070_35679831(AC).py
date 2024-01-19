#월이 입력될 때 계절 이름이 출력되도록 해보자.

#월 : 계절 이름
#12, 1, 2 : winter
  #3, 4, 5 : spring
  #6, 7, 8 : summer
  #9, 10, 11 : fall


n = int(input())  # 월을 입력받습니다.

if n == 12 or n == 1 or n == 2:
    print("winter")
else:
    if n == 3 or n == 4 or n == 5:
        print("spring")
    else:
        if n == 6 or n == 7 or n == 8:
            print("summer")
        else:
            if n == 9 or n == 10 or n == 11:
                print("fall")
