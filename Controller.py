from VIEWS import *
from MODELS import *


def path(palabra):
    
    if palabra == "first":
        var = firstview.firstscreen("Bienvenido")
    elif palabra == "logscreen":
        var = logview.loginscreen("login")
    elif palabra == "userscreen":
        var = userview.userscreen("Menu usuario")
    elif palabra == "dogscreen":
        var = dogsview.dogscreen("Tus perros")
    return var

def main():
    current = path("first")
    estado = True
    user = None

    while estado:
        order = current.makeit()
        if isinstance(order, str):
            if order == "salir":
                current.salir()
                estado = False
            else:
                current.salir()
                current = path(order)

        else:
            if order[0] == "userlog":
                user = model.userlog(order[1], order[2])
                if not (user == None):
                    current.salir()
                    current = path("userscreen")
                else:
                    current.error()
                    current.salir()
                    current = logview.loginscreen("Vuelva a intentar")
            if order[0] == "dogscreen":
                dogs = model.dogbyuser(user.id)
                current.salir()
                current = dogsview.dogscreen("Tus perros", dogs)

if __name__ == "__main__":
    main()
