x=0
y=0
p="да"
while not(p=="нет"):
    k=str(input("Куда? : " ))
    s=int(input("На сколько? : " ))
    if(k=="вправо" or k=="влево"):
        if(k=="вправо"):
            x= x+(s)
        else:
            x=x+(-s)
    else:
        if(k=="вверх"):
            y= y+(s)
        else:
            y=y+(-s)
    print("Новая позция: ({0};{1})" .format(x,y))
    p= input("Продолжить ввод? : ")
    