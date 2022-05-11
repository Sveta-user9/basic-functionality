class Product():
    print("Список товара:")
    def creat_p(self,name,prise,quantity): #функция Создает список с именем продукта, его ценой и кол-вом.
        self.name=name
        self.prise=0
        self.quantity=0
        product.append(name)
        product.append('-')
        product.append(prise)
        product.append('грн,')
        product.append(quantity)
        product.append('шт|')
    def chec_input(self):
        """проверяет есть ли продукт в списке"""
        global prise
        global quantity
        global index_quantity
        while True:
            print("\n что хотите купить?", "\t (Если хотите остановить программу, введите \"stop\")")
            order = (input())
            if order in product:
                index_prise = 2 + product.index(order)
                index_quantity = 4 + product.index(order)
                prise = product[index_prise]  # Цена из списка
                quantity = product[index_quantity]  # кол-во из списка
                if quantity <= 0:
                    print("Нету в наличии.")
                    Product().new_creat_p()
                    continue
                print("Оплатите", prise, "грн", "Остаток-", quantity, "шт")
                for x in list_bill:# из класса Pay. Печатает досупные кпюры для оплаты
                    print("\t\tДля внесения доступны такие купюры (в грн):",x)
                Pay().depositing_money()
            elif order == "stop":
                print("End")
                break
            else:
                print("Вы ввели несуществующий товар. Повторите попытку")
    def new_creat_p(self):          #функция должна показывать список product, где quantity-1
        if quantity <= 0:
            for x in product:
                print(x, end=' ')
        else:
            product[index_quantity] = int(quantity) - 1
            for x in product:
                print(x, end=' ')
class Pay():
    global sum_buer
    def creat_bill(self, *bill):
        list_bill.append(bill)
    def depositing_money(self): #функция внесения денег.
        kupur = input("\tВведите, пожалуйста, купюры для оплаты через пробел ").split()
        s = list(map(int, kupur))
        sum_buer = (sum(s))
        def print_change():
            def pc():
                if dr not in chn:
                    chn.append(dr)
                    for x in chn:
                        print("Ваша сдача ", str(x), sep=' ')
            change = (int(sum_buer) - int(prise))
            ch=[5,10,20,50,100,200,500,1000]#[1000, 500, 200, 100, 50, 20, 10, 5]
            chn=[]
            for bill in ch:
                if change == bill:
                    print("Ваша сдача ",bill)
                for i in (ch):
                    for j in (ch):
                        if j + i == change:
                            dr = sorted((i, j))
                            pc()
                        for k in (ch):
                            if j + i + k == change:
                                dr = sorted((i, j, k))
                                pc()
                            for l in (ch):
                                if j + i + k + l  == change:
                                    dr = sorted((i, j, k, l))
                                    pc()
                                for l2 in (ch):
                                    if j + i + k +l+ l2== change:
                                        dr = sorted((i, j, k, l, l2))
                                        pc()
        if sum_buer == prise:# prise - это глобальня переменная из def chec_input(self). Product().
            print("\tОплата пройдена успешно!\n")
            Product().new_creat_p() #выводить список оставшихся товаров. (функция new_creat_p() из  Product())
        elif sum_buer > prise:
            print()
            print_change()
            Product().new_creat_p()
        while sum_buer < prise:
            print("ВНИМАНИЕ! \n Не хватает денег! Доплатите " + str(prise - sum_buer) + "грн")
            kupur = input("Введите, пожалуйста, полученые купюры через пробел ").split()
            s1 = list(map(int, kupur))
            s += s1
            sum_buer = (sum(s))
            if sum_buer>prise:
                print_change()
            Product().new_creat_p()

list_bill = []
Pay().creat_bill(1000,500,200,100,50,20,10,5)
"""купюры"""
product=[]
Product().creat_p("Яблоко",5,1)
Product().creat_p("Морожено",10,5)
Product().creat_p("Конфеты",25,10)
Product().creat_p("Молоко",30,25)
for x in product:
    print(x, end=' ')
"""выводит список товаров актуальный"""
Product().chec_input()
"""Вводим товар, который надо преобрести."""