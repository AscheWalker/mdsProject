from graphics import *
from button import Button
from found import found
from login import login


def create():
    print(3)

def main():
    win = GraphWin("sistema perro", 600, 600)
    win.setCoords(0,0,10,10)
    win.setBackground("white")

    #button to find the owner of a dog
    butFound = Button(win, Point(5, 7), 4, 1, "Encontre un perro")
    butFound.activate()
    
    #button to login
    butLogin = Button(win, Point(5, 5), 4, 1, "Ingresar como usuario")
    butLogin.activate()

    #button to create user
    butCreate = Button(win, Point(5, 3), 4, 1, "Crear usuario")
    #butCreate.activate()
    
    #button to exit the application
    butExit = Button(win, Point(8, 1), 2, 0.5, "Salir")
    butExit.rect.setFill('red')
    butExit.activate()

    mc = win.getMouse()

    while not butExit.clicked(mc):

        #click in "I found a dog"
        if butFound.clicked(mc):
           found()

        #click in "Log as user"
        elif butLogin.clicked(mc):
            login()


        #click in "Create user"
        elif butCreate.clicked(mc):
            create()

        mc = win.getMouse()



    win.close()


main()
