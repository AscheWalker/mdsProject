if __name__ == '__main__':
    from graphicskyo import *
    from button import Button
    from base import wind
else:
    from .graphicskyo import *
    from .button import Button
    from .base import wind


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



class loginscreen(wind):

    def makeit(self):
        self.userField = Entry(Point(3, 7), 15)
        self.userField.draw(self.win)
        self.userText = Text(Point(7, 7), "Ingrese su usuario")
        self.userText.draw(self.win)
        self.pwdField = Entry(Point(3, 5), 15)
        self.pwdField.draw(self.win)
        self.pwdText = Text(Point(7, 5), "Ingrese su clave")
        self.pwdText.draw(self.win)

        self.doneText = Text(Point(5, 9), "usuario o clave incorrecto")
        self.doneText.setSize(20)
        self.doneText.setTextColor('red')

        self.loginButt = Button(self.win, Point(2, 1), 1.3, 1, "Login")
        self.loginButt.activate()

        self.mc = self.win.getMouse()

        while not self.butExit.clicked(self.mc):

            if self.loginButt.clicked(self.mc):
            
                return ["userlog", self.userField.getText(), self.pwdField.getText()]
                    

            self.mc = self.win.getMouse()



    def error(self):
        self.doneText.undraw()
        self.doneText.draw(self.win)
            
