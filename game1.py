import random as rd
list=[]
while len(list)!=3:
    a=rd.randint(1,3)
    if a in list:
        pass
    else:
        list.append(a)
list.append(' ')
def win():
    if list[0]==1 and list[1]==2 and list[2]==3 and list[3]==' ':
        print("you won the game.congratulations !")
        ch=input("do you want to play again (y/n)")
        if ch=='y':
            game()  
    else:
        return game()
            
def game():
    print('                               ','-'*27)
    print('                               ','|',' BOX NO-1 ','|',' BOX NO-2 ','|')
    print('                               ','|','          ','|','          ','|')
    print('                               ','|','    %s     '%list[0],'|','      %s   '%list[1],'|'   )
    print('                               ','|','          ','|','          ','|')
    print('                               ','-'*27)        
    print('                               ','|','  BOX NO-3','|','          ','|')
    print('                               ','|','          ','|','          ','|')
    print('                               ','|','    %s     '%(list[2]),'|','    %s     '%list[3],'|'   )
    print('                               ','|','          ','|','          ','|')
    print('                               ','-'*27)
    print()
    num=input("choose the box no you want to move= ")
    if num=='1':
        m=list[0]
        if list[1]==' ':
            list[1]=m
            list[0]=' '
        elif list[2]==' ':
            list[2]=m
            list[0]=' '
        else:
            print("\nYou can't go anywhere . Try again")
        win()
    elif num=='2':
        m=list[1]
        if list[0]==' ':
            list[0]=m
            list[1]=' '
        elif list[3]==' ':
            list[3]=m
            list[1]=' '
        else:
            print("\nYou can't go anywhere. Try again")
        win()
    elif num=='3':
        m=list[2]
        if list[0]==' ':
            list[0]=m
            list[2]=' '
        elif list[3]==' ':
            list[3]=m
            list[2]=' '
        else:
            print("\nYou can't go anywhere. Try again")
        win()
        
    elif num=='4':
        m=list[3]
        if list[1]==' ':
            list[1]=m
            list[3]=' '
        elif list[2]==' ':
            list[2]=m
            list[3]=' '
        else:
            print("\nYou can't go anywhere. Try again")
        win()    
