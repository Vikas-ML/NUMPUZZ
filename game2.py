import random as rd
list=[]
while len(list)!=8:
    a=rd.randint(1,8)
    if a in list:
        pass
    else:
        list.append(a)
list.append(' ')
def win():
    if list[0]==1 and list[1]==2 and list[2]==3 and list[3]==4 and list[4]==5 and list[5]==6 and list[6]==7 and list[7]==8 and list[8]==' ':
        print("you won the game.congratulations !")
        ch=input("do you want to play again (y/n")
        if ch=='y':
            game()  
    else:
        return game()
def game():

    print('                               ','-'*39)
    print('                               ','|',' BOX NO-1 ','|',' BOX NO-2 ','|',' BOX NO-3','|')
    print('                               ','|','          ','|','          ','|','         ','|')
    print('                               ','|','   %s      '%(list[0]),'|','    %s     '%list[1],'|','    %s    '%list[2],'|')
    print('                               ','|','          ','|','          ','|','         ','|')
    print('                               ','-'*39)
    print('                               ','|',' BOX NO-4 ','|',' BOX NO-5 ','|',' BOX NO-6','|')
    print('                               ','|','          ','|','          ','|','         ','|')
    print('                               ','|','   %s      '%(list[3]),'|','    %s     '%list[4],'|','    %s    '%list[5],'|')
    print('                               ','|','          ','|','          ','|','         ','|')
    print('                               ','-'*39)
    print('                               ','|',' BOX NO-7 ','|',' BOX NO-8 ','|',' BOX NO-9','|')
    print('                               ','|','          ','|','          ','|','         ','|')
    print('                               ','|','   %s      '%(list[6]),'|','    %s     '%list[7],'|','    %s    '%list[8],'|')
    print('                               ','|','          ','|','          ','|','         ','|')
    print('                               ','-'*39)
    print()
    num=input("choose the box no you want to move= ")
    if num=='1':
        m=list[0]
        if list[1]==' ':
            list[1]=m
            list[0]=' '
        elif list[3]==' ':
            list[3]=m
            list[0]=' '
        else:
            print("\nYou can't go anywhere . Try again")
        win()
    elif num=='2':
        m=list[1]
        if list[0]==' ':
            list[0]=m
            list[1]=' '
        elif list[2]==' ':
            list[2]=m
            list[1]=' '
        elif list[4]==' ':
            list[4]=m
            list[1]=' '
        else:
            print("\nYou can't go anywhere. Try again")
        win()
    elif num=='3':
        m=list[2]
        if list[1]==' ':
            list[1]=m
            list[2]=' '
        elif list[5]==' ':
            list[5]=m
            list[2]=' '
        else:
            print("\nYou can't go anywhere. Try again")
        win()
        
    elif num=='4':
        m=list[3]
        if list[0]==' ':
            list[0]=m
            list[3]=' '
        elif list[4]==' ':
            list[4]=m
            list[3]=' '
        elif list[6]==' ':
            list[6]=m
            list[3]=' '
        else:
            print("\nYou can't go anywhere. Try again")
        win()
    elif num=='5':
        m=list[4]
        if list[3]==' ':
            list[3]=m
            list[4]=' '
        elif list[7]==' ':
            list[7]=m
            list[4]=' '
        elif list[5]==' ':
            list[5]=m
            list[4]=' '
        elif list[1]==' ':
                list[1]=m
                list[4]=' '
        else:
            print("\nYou can't go anywhere. Try again")
        win()
        
    elif num=='6':
        m=list[5]
        if list[4]==' ':
            list[4]=m
            list[5]=' '
        elif list[8]==' ':
            list[8]=m
            list[5
                 ]=' '
        elif list[2]==' ':
            list[2]=m
            list[5]=' '
        else:
            print("\nYou can't go anywhere. Try again")
        win()
    elif num=='7':
        m=list[6]
        if list[3]==' ':
            list[3]=m
            list[6]=' '
        elif list[7]==' ':
            list[7]=m
            list[6]=' '
        else:
            print("\nYou can't go anywhere. Try again")
    
        win() 
    elif num=='8':
        m=list[7]
        if list[8]==' ':
           list[8]=m
           list[7]=' '
        elif list[4]==' ':
            list[4]=m
            list[7]=' '
        elif list[6]==' ':
            list[6]=m
            list[7]=' '
        else:
            print("\nYou can't go anywhere. Try again")      

        win()
    elif num=='9':
        m=list[8]
        if list[5]==' ':
            list[5]=m
            list[8]=' '
        elif list[7]==' ':
            list[7]=m
            list[8]=' '
        else:
            print("\nYou can't go anywhere. Try again")
        win()
    
