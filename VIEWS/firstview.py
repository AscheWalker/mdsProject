if __name__ == '__main__':
    from graphicskyo import *
    from button import Button
    from base import wind
else:
    from .graphicskyo import *
    from .button import Button
    from .base import wind



class firstscreen(wind):

    def makeit(self):
        #button to login
        self.butLogin = Button(self.win, Point(5, 5), 4, 1, "Ingresar como usuario")
        self.butLogin.activate()

        #button to create user
        self.butCreate = Button(self.win, Point(5, 3), 4, 1, "Crear usuario")
        self.butCreate.activate()
        
        

        self.mc = self.win.getMouse()

        while not self.butExit.clicked(self.mc):

            #click in "Log as user"
            if self.butLogin.clicked(self.mc):
                return "logscreen"


            #click in "Create user"
            elif self.butCreate.clicked(self.mc):
                return "createscreen"

            self.mc = self.win.getMouse()

        return "salir"

if __name__ == '__main__':
    test = firscreen("test")
    test.makeit()
