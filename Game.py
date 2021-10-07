def numpuz():
    
    print("                     ","WELCOME IN OUR GAME")
    print()
    print("                     ","1.PRESS 1 FOR EASY(2X2)")
    print("                     ","2.PRESS 2 FOR MEDIUM(3X3)")
    print("                     ","3.PRESS 3 FOR HARD(4X4)")
    ch=input("enter your choice= ")
    while ch.isdigit() != True:
            print("enter in integer format")
            ch= input("enter your age")
    else:
         print()
    if ch=='1':
        import game1 as g
        g.game()
    elif ch=='2':
        import game2 as g
        g.game()
    elif ch=='3':
        import game3 as g
        g.game()
    else:
        print("YOU HAVE TO CHOOSE ANY ONE TO PLAY THE GAME")

numpuz()        
    
