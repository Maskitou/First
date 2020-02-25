import random
how_many_sticks = 21
robot = 'RD2'
while True:
    N = int(input("Ваш ход: "))
    while N > 3 or N < 1 or N == str:
        N=int(input("Неверный ввод, попробуйте снова: "))
    else:
        how_many_sticks-= N
        if how_many_sticks <= 0:
            print("ВЫ ВЫИГРАЛИ!")
            break
        else:
            print("Осталось", how_many_sticks, "палочек")
    n = random.randint(1,3)
    print('Ход робота:',n)
    how_many_sticks -=n
    print("Осталось",how_many_sticks,"палочек")
    if how_many_sticks <= 0:
        print("Победил", robot)
        break