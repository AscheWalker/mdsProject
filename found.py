from graphics import *
from button import Button
from buscar import dogfind
from msn import sendmsg


def found():
    win = GraphWin("Identificacion perro", 400, 200)
    win.setCoords(0,0,10,10)
    win.setBackground("white")

    dogField = Entry(Point(3, 8), 10)
    dogField.draw(win)
    dogText = Text(Point(6, 8), "Ingrese id del perro")
    dogText.draw(win)

    buscarButt = Button(win, Point(2, 1), 1.3, 1, "Buscar")
    buscarButt.activate()

    

    #button to exit the application
    butExit = Button(win, Point(8, 1), 2, 1, "Salir")
    butExit.rect.setFill('red')
    butExit.activate()

    mode = 1

    mc = win.getMouse()

    while not butExit.clicked(mc):

        if buscarButt.clicked(mc):
            if mode == 1:
                dog = dogfind(dogField.getText())
                print(dog)
                if not (dog == None):
                    dogField.undraw()
                    dogText.undraw()
                    msgField = EntryBox(Point(5, 6), 40, 6)
                    msgField.draw(win)
                    buscarButt.label.setText("Enviar")
                    mode = 2
                    
            elif mode == 2:
                sendmsg(dog.owner, dog.id, msgField.getText())
                msgField.undraw()
                buscarButt.deactivate()
                doneText = Text(Point(5, 6), "El mensaje fue enviado")
                doneText.setSize(20)
                doneText.draw(win)

        mc = win.getMouse()



    win.close()

