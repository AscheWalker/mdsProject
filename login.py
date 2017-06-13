from graphics import *
from button import Button
from buscar import *



def seeDogs(userId):
    print("seeDogButt placeholder")
    mac = GraphWin("Tus perros", 400, 200)
    mac.setCoords(0,0,10,10)
    mac.setBackground("white")
    dogs = dogbyuser(userId)
    va = 7
    for dog in dogs:
        Text(Point(5, va), dog.name).draw(mac)
        va = va - 1

def addDogs():
    print("addDog placeholder")



def login():
    win = GraphWin("Login", 400, 200)
    win.setCoords(0,0,10,10)
    win.setBackground("white")

    userField = Entry(Point(3, 7), 15)
    userField.draw(win)
    userText = Text(Point(7, 7), "Ingrese su usuario")
    userText.draw(win)
    pwdField = Entry(Point(3, 5), 15)
    pwdField.draw(win)
    pwdText = Text(Point(7, 5), "Ingrese su clave")
    pwdText.draw(win)

    loginButt = Button(win, Point(2, 1), 1.3, 1, "Login")
    loginButt.activate()

    

    #button to exit the application
    butExit = Button(win, Point(8, 1), 2, 1, "Salir")
    butExit.rect.setFill('red')
    butExit.activate()

    doneText = Text(Point(5, 9), "usuario o clave incorrecto")
    doneText.setSize(20)
    doneText.setTextColor('red')

    mc = win.getMouse()

    while not butExit.clicked(mc):

        if loginButt.clicked(mc):
        
            user = userlog(userField.getText(), pwdField.getText())
            if not (user == None):
                userField.undraw()
                userText.undraw()
                pwdField.undraw()
                pwdText.undraw()
                doneText.undraw()
                loginButt.deactivate()
                
                #button to see user dogs
                seeDogButt = Button(win, Point(5, 7), 4, 1, "ver perros")
                seeDogButt.activate()
 
                #button to add a dog
                addDogButt = Button(win, Point(5, 5), 4, 1, "Agregar perro")
                #addDogButt.activate()


                mc = win.getMouse()

                while not butExit.clicked(mc):
                    if seeDogButt.clicked(mc):
                        seeDogs(user.id)
                    elif addDogButt.clicked(mc):
                        addDogs()
                    mc = win.getMouse()
                break
                
            else:
                doneText.undraw()
                doneText.draw(win)

        mc = win.getMouse()



    win.close()

