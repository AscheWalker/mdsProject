if __name__ == '__main__':
    from graphicskyo import *
    from button import Button
    from base import wind
else:
    from .graphicskyo import *
    from .button import Button
    from .base import wind
from tkinter import messagebox

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

        self.loginButt = Button(self.win, Point(2, 1), 1.3, 1, "Login")
        self.loginButt.activate()

        self.mc = self.win.getMouse()

        while not self.butExit.clicked(self.mc):

            if self.loginButt.clicked(self.mc):
            
                return ["userlog", self.userField.getText(), self.pwdField.getText()]
                    

            self.mc = self.win.getMouse()
        
        return "first"


    def error(self):
        messagebox.showinfo("Error", "usuario o clave incorrecto")
            
