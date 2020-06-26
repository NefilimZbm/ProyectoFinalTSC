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
T: float
flag: bool = False
origin: str = ""
des: str = ""
T=process_time()
city: dict = dict(  # X = nombre [0], Vecinos [1], Coordenadas [2], Hijos [3], Distancia [4]
    A=["Acayucan", ['M', 'Sat', 'N'], [17.94919, -94.91459], None, 0],
    B=["Boca del río", ['Alv', 'J', 'X', 'Z'], [19.10627, -96.10632], None, 0],
    C=["Coatzacoalcos", ['AD', 'M', 'Sat'], [18.13447, -94.45898], None, 0],
    AD=["Agua Dulce", ['C'], [18.14259, -94.1436], None, 0],
    HJ=["Huatla de Jiménez", ['O', 'F'], [18.13108, -96.84314], None, 0],
    F=["Fortín de las Flores", ['HJ', 'Y', 'H'], [18.9017, -96.99896], None, 0],
    H=["Huatusco", ['F', 'X'], [19.14823, -96.96654], None, 0],
    J=["Joachín", ['O', 'B', 'Y'], [18.6407, -96.23095], None, 0],
    M=["Minatitlán", ['C', 'A'], [17.99392, -94.5466], None, 0],
    N=["El Nigromante", ['A', 'O'], [17.76323, -95.75574], None, 0],
    O=["Otatitlán", ['N', 'Alv', 'J', 'HJ'], [18.18106, -96.03439], None, 0],
    P=["Papantla", ['Tec', 'V', 'Tez'], [20.45667, -97.31561], None, 0],
    Alv=["Alvarado", ['Sat', 'O', 'B'], [18.76961, -95.75894], None, 0],
    Tec=["Tecolutla", ['P', 'V'], [20.47955, -97.01012], None, 0],
    Tez=["Teziutlán", ['P', 'X'], [19.81601, -97.35705], None, 0],
    Sat=["San Andrés Tuxtla", ['C', 'A', 'Alv'], [18.44412, -95.21302], None, 0],
    V=["Vega de Alatorre", ['Tec', 'P', 'X', 'Z'], [20.03034, -96.65044], None, 0],
    X=["Xalapa", ['Tez', 'V', 'Z', 'B', 'H'], [19.54377, -96.91018], None, 0],
    Y=["Yanga", ['F', 'J'], [18.82928, -96.80027], None, 0],
    Z=["Zempoala", ['B', 'X', 'V'], [19.44688, -96.40507], None, 0]
)

cost: dict = dict(  # [vecino, costo al vecino]
    A=[['M', 78], ['Sat', 0], ['N', 0.0]],
    B=[['Alv', 0], ['J', 108], ['X', 99], ['Z', 0.0]],
    C=[['AD', 22], ['M', 0], ['Sat', 78]],
    AD=['C', 22],
    HJ=[['O', 0.0], ['F', 14]],
    F=[['HJ', 14], ['Y', 0], ['H', 0]],
    H=[['F', 0], ['X', 36]],
    J=[['O', 0.0], ['B', 108], ['Y', 78]],
    M=[['C', 0], ['A', 78]],
    N=[['A', 0.0], ['O', 0.0]],
    O=[['N', 0.0], ['Alv', 0.0], ['J', 0.0], ['HJ', 0.0]],
    P=[['Tec', 0], ['V', 0.0], ['Tez', 0]],
    Alv=[['Sat', 24], ['O', 0.0], ['B', 0]],
    Tec=[['P', 0], ['V', 0.0]],
    Tez=[['P', 0], ['X', 149]],
    Sat=[['C', 78], ['A', 0], ['Alv', 24]],
    V=[['Tec', 0.0], ['P', 0.0], ['X', 0.0], ['Z', 0.0]],
    X=[['Tez', 149], ['V', 0.0], ['Z', 0.0], ['B', 99], ['H', 36]],
    Y=[['F', 0], ['J', 78]],
    Z=[['B', 0.0], ['X', 0.0], ['V', 0.0]]
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
                ##
                for k in cost[i]:
                    if k[0] == i:
                        if k[1]==None:
                            city[i][4] = int(ft.distance(city[i][2], city[des][2]))
                            print("Solo distancia")
                        else:
                            city[i][4] = int(ft.distance(city[i][2], city[des][2])) + int(k[1])
                            print("costo:  ",k[1])
                #city[i][4] = ft.distance(city[i][2], city[des][2])
                if li == []:
                    li.append(i)
                    print("primero  ",li)
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
                    print("en bucle", li)
                    while ld != []:
                        li.append(ld[-1])
                        ld.pop(-1)
        city[route[-1]][3] = li
        print("final ",li)
        route.append(li[-1])
        li = []
print("         Recorrido: ")
for i in route:
    print("              ", city[i][0])
print("Tiempo de cómputo en segundos es:    ", process_time()-T)