from math import sin
from math import asin
from math import sqrt
from math import pi
from time import process_time
from typing import List
from Modules import functions as ft

print("Este programa genera un ruta entre dos de las siguientes posibles ciudades:")
print("A para Acayucan\nB para Boca del Río\nC para Coatzacoalcos\nAD para Agua Dulce\nHJ para Huatla de Jiménez\n"
      "F para Fortín de las Flores\nH para Huatusco\nJ para Joachín\nM para  Minatitlan\nN para El Nigromante\n"
      "O para Otatitlán\nP para Papantla\nAlv para Alvarado\nTec para Tecolutla\nTez para Teziutlán\n"
      "Sat para San Andrés Tuxtla\nV para Vega de Alatorre\nX para Xalapa\nY para Yanga\nZ para Zempoala")

# variables a declarar
route: List = []
lv: List = []
name_city: List = ["A", "B", "C", "AD", "HJ", "F", "H", "J", "M", "N", "O", "P", "Alv", "Tec", "Tez", "Sat", "V", "X",
                   "Y", "Z"]
li: List = []
ld: List = []
flag: bool = False
origin: str = ""
des: str = ""
t: float = process_time()
city: dict = dict(  # X = nombre [0], Vecinos [1], Coordenadas [2], Hijos [3], Distancia [4]
    A=["Acayucan", ['M', 'Sat', 'N'], [17.94919, -94.91459], None, None],
    B=["Boca del río", ['Alv', 'J', 'X', 'Z'], [19.10627, -96.10632], None, None],
    C=["Coatzacoalcos", ['AD', 'M', 'Sat'], [18.13447, -94.45898], None, None],
    AD=["Agua Dulce", ['C'], [18.14259, -94.1436], None, None],
    HJ=["Huatla de Jiménez", ['O', 'F'], [18.13108, -96.84314], None, None],
    F=["Fortín de las Flores", ['HJ', 'Y', 'H'], [18.9017, -96.99896], None, None],
    H=["Huatusco", ['F', 'X'], [19.14823, -96.96654], None, None],
    J=["Joachín", ['O', 'B', 'Y'], [18.6407, -96.23095], None, None],
    M=["Minatitlán", ['C', 'A'], [17.99392, -94.5466], None, None],
    N=["El Nigromante", ['A', 'O'], [17.76323, -95.75574], None, None],
    O=["Otatitlán", ['N', 'Alv', 'J', 'HJ'], [18.18106, -96.03439], None, None],
    P=["Papantla", ['Tec', 'V', 'Tez'], [20.45667, -97.31561], None, None],
    Alv=["Alvarado", ['Sat', 'O', 'B'], [18.76961, -95.75894], None, None],
    Tec=["Tecolutla", ['P', 'V'], [20.47955, -97.01012], None, None],
    Tez=["Teziutlán", ['P', 'X'], [19.81601, -97.35705], None, None],
    Sat=["San Andrés Tuxtla", ['C', 'A', 'Alv'], [18.44412, -95.21302], None, None],
    V=["Vega de Alatorre", ['Tec', 'P', 'X', 'Z'], [20.03034, -96.65044], None, None],
    X=["Xalapa", ['Tez', 'V', 'Z', 'B', 'H'], [19.54377, -96.91018], None, None],
    Y=["Yanga", ['F', 'J'], [18.82928, -96.80027], None, None],
    Z=["Zempoala", ['B', 'X', 'V'], [19.44688, -96.40507], None, None]
)

while not flag:
    origin: str = str(input("Nombre de la ciudad de origen"))
    for i in name_city:
        if i == origin:
            flag = True
    if not flag:
        print("No es una entrada válida, vuelve a intentarlo")
flag = False

while not flag:
    des: str = str(input("Nombre de la ciudad destino"))
    for i in name_city:
        if i == des:
            flag = True
    if not flag:
        print("No es una entrada válida, vuelve a intentarlo")

if des == origin:
    print("Origen y destino iguales, acabamos")
else:
    route.append(origin)
    while route[-1] != des:
        lv = city[route[-1]][1]
        for i in lv:
            flag = False
            for j in route:
                if i == j:
                    flag = True
            if not flag:
                city[i][4] = ft.distance(city[i][2], city[des][2])
                if li == []:
                    li.append(i)
                else:
                    while not flag:
                        if city[i][4] >= city[li[-1]][4]:
                            ld.append(li[-1])
                            li.pop(-1)
                            if li == []:
                                flag = True
                        else:
                            flag = True
                    li.append(i)
                    while ld != []:
                        li.append(ld[-1])
                        ld.pop(-1)
        city[route[-1]][3] = li
        route.append(li[-1])
        li = []
print("         Recorrido: ")
for i in route:
    print("              ", city[i][0])

print("Tiempo de cómputo en segundos es:    ", process_time()-t)

