from operator import itemgetter

ves_inventory = 10
inventory = []
def addinventory(func):
    global ves_inventory
    global inventory
    if ves_inventory-func.get("ves") >= 0:
        ves_inventory -= func.get("ves")
        inventory.append(item)
        print("Вы добавили:", func.get("name"))
        
    else:
        print("Инвентарь перполнен, невозможно добавить предмет")
        exit
def removeinventory():
    global ves_inventory
    global inventory
    print("Ваш инветарь:", inventory)
    choice = (input("Что вы хотите убрать? \n"))
    inventory.remove(choice)
    ves_inventory += item.get("ves")

while True:
    print("Оставшийся вес =", ves_inventory)
    print("Добавить или Убрать")
    y = int(input("Что вы хотите сделать? (выберите 1 или 2) \n" ))

    if y == 1:
        x = str(input("Что вы хотите добавить в инвентарь? \n"))
        v = int(input("Какой вес у добавляемого предмета? \n"))
        item = {"name":x,"ves":v}
        addinventory(item)
        print("Ваш инвентарь:")
        
        getvalues = itemgetter("name", "ves") 
        for d in inventory:
               print(*getvalues(d))

    elif y == 2:
        if ves_inventory == 10:
            print("Инвентарь пуст")
        else:
            removeinventory()
    else:
        print(" ")
