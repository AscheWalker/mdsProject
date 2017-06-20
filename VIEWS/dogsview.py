if __name__ == '__main__':
    from graphicskyo import *
    from button import Button
    from base import wind
else:
    from .graphicskyo import *
    from .button import Button
    from .base import wind



class dogscreen(wind):
    def __init__(self, titulo, dogs):
        self.win = GraphWin(titulo, 600, 600)
        self.win.setCoords(0,0,10,10)
        self.win.setBackground("white")
        self.dogs = dogs

        #button to exit the application
        self.butExit = Button(self.win, Point(8, 1), 2, 0.5, "Salir")
        self.butExit.rect.setFill('red')
        self.butExit.activate()

    def makeit(self):
        self.va = 7
        for dog in self.dogs:
            Text(Point(5, self.va), dog.name).draw(self.win)
            self.va = self.va - 1

        self.mc = self.win.getMouse()

        while not self.butExit.clicked(self.mc):
            self.mc = self.win.getMouse()
            

        return "userscreen"
