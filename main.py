while True:
    ais = ["Ескимо", "пломбир с клубникой", "шоколадная березка"]
    prise = [25, 10, 35]
    c = []
    i = 0
    j = 0
    while i < len(ais) and j < len(prise):
        c.append(ais[i])
        c.append("-")
        i += 1
        c.append(prise[j])
        c.append('грн;')
        j += 1
    print("\tCписок мороженого в грн:")
    for x in c:
        print(x, end=" ")
    print('\n \tЧто хотите купить?')

    order = str(input())
    payment = 0
    if order == ais[-1]:
        payment += prise[-1]
        print("К оплате " + str(payment) + " грн ")
    elif order == ais[-2]:
        payment += prise[-2]
        print("К оплате " + str(payment) + " грн ")
    elif order == ais[-3]:
        payment += prise[-3]
        print("К оплате " + str(payment) + " грн ")
    elif order == '0':
        break
    else:
        print(order + " нету в наличии ((")
        continue

    print("\n для внесения доступны такие купюры: 5 10 20 50 100 200 500 1000 грн.")
    kupur = input("Введите, пожалуйста, полученые купюры через пробел ").split()
    s = list(map(int, kupur))
    sum_buer = (sum(s))
    def print_change():
        change = (int(sum_buer) - int(payment))
        ch = [5, 10, 20, 50, 100, 200, 500, 1000]
        chn = []
        for i in (ch):
            for j in (ch):
                for k in (ch):
                    if i + j + k == change:
                        dr = sorted((i, j, k))
                        if dr not in chn:
                            chn.append(dr)
                            for x in chn:
                                print("Ваша сдача ", str(x))
                                print("\tOстаток в кассе: " + (new_kassa + " грн"))

    kassa = 1000
    kassa2 = kassa + sum_buer
    change = (int(sum_buer) - int(payment))
    new_kassa = str(kassa2 - int(change)) #+ int(sum_buer))
    for x in s:
        if x == 5 or x == 10 or x == 20 or x == 50 or x == 100 or x == 200 or x == 500 or x == 1000:
            if sum_buer == payment:
                print("\tOстаток в кассе: " + (new_kassa + " грн"))
                n_s=0
            while sum_buer < payment:
                print("ВНИМАНИЕ! \n Не хватает денег! Доплатите " + str(payment - sum_buer) + "грн")
                kupur = input("Введите, пожалуйста, полученые купюры через пробел ").split()
                s1 = list(map(int, kupur))
                s+=s1
                sum_buer = (sum(s))
            if sum_buer > payment:
                print_change()
        else:
            print("\t\t!!Эта купюра не принимается")
