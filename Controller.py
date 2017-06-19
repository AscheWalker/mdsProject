from VIEWS import *
from MODELS import *


def path(palabra):

    dicpath = dict([
        ("logscreen", logview.loginscreen("login")),
        ("createscreen", "placeholder")
        ])

    return dicpath[palabra]

current = firstview.firstscreen("Bienvenido")

estado = True

while estado:
    order = current.makeit()
    if isinstance(order, str):
        if order == "salir":
            current.salir()
        else:
            current = path(order)

    else:
        if order[0] == "userlog":
            user = model.userlog(order[1], order[2])
            if not (user == None):
                print(None) 
            else:
                current.error()
