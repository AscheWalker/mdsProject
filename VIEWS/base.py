if __name__ == '__main__':
    from graphicskyo import *
    from button import Button
else:
    from .graphicskyo import *
    from .button import Button

class wind:

    def __init__(self, titulo):
        self.win = GraphWin(titulo, 600, 600)
        self.win.setCoords(0,0,10,10)
        self.win.setBackground("white")

        #button to exit the application
        self.butExit = Button(self.win, Point(8, 1), 2, 0.5, "Salir")
        self.butExit.rect.setFill('red')
        self.butExit.activate()


    def enviar(self, orden):
        return orden

    def salir(self):
        self.win.close()
