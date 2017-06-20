if __name__ == '__main__':
    from graphicskyo import *
    from button import Button
    from base import wind
else:
    from .graphicskyo import *
    from .button import Button
    from .base import wind

class userscreen(wind):
    def makeit(self):
        #button to see user dogs
        self.seeDogButt = Button(self.win, Point(5, 7), 4, 1, "ver perros")
        self.seeDogButt.activate()
     
        #button to add a dog
        self.addDogButt = Button(self.win, Point(5, 5), 4, 1, "Agregar perro")
        #self.addDogButt.activate()


        self.mc = self.win.getMouse()

        while not self.butExit.clicked(self.mc):
            if self.seeDogButt.clicked(self.mc):
                return ["dogscreen", "nada"]
            elif self.addDogButt.clicked(self.mc):
                return "addDogs"
            mc = win.getMouse()

        return "salir"
