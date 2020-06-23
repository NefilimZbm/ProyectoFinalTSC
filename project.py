from math import sin
from math import asin
from math import sqrt
from math import pi
from Modules import functions as ft

# Esto puede que mejor vaya en el Readme
print("Este programa genera un ruta entre dos de las siguientes  posibles ciudades de Veracruz:")
print("A para Acayucan\n",
      "B para Boca del río\n",
      "C para Coatzacoalcos\n",
      "AD para Agua Dulce\n",
      "HJ para Huatla de Jiménez\n",
      "F para Fortín de las Flores\n",
      "H para Huatusco\n",
      "J para Joachín\n",
      "M para  Minatitlan\n",
      "N para El Nigromante\n",
      "O para Otatitlán\n",
      "P para Papantla\n",
      "Alv para Alvarado\n",
      "Tec para Tecolutla\n",
      "Tez para Teziutlán\n",
      "Sat para San Andrés Tuxtla\n",
      "V para Vega de Alatorre\n",
      "X para Xalapa\n",
      "Y para Yanga\n",
      "Z para Zempoala")
#####################################################################################################
# Variables a declarar
Recorrido = []  # lista
Lv = []  # Lista
L = ["A", "B", "C", "A", "D", "HJ", "F", "H", "J", "M", "N", "O", "P", "Alv", "Tec", "Tez", "Sat", "V", "X", "Y", "Z"]
L_i = []  # lista
L_d = []  # lista
flag = False  # flag = boleano

city = dict(  # X = nombre [0], Vecinos [1], Coordenadas [2], Hijos [3], Distancia [4]
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

while flag != True:
    Origen = input("Nombre de la ciudad de origen")
    for l in L:
        if l == Origen:
            flag = True
    else:
        print("No es una entrada válidad, vuelve a intentarlo")
flag = False
while flag != True:
    Destino = input("Nombre de la ciudad destino")
    for l in L:
        if l == Destino:
            flag = True
    else:
        print("No es una entrada válidad, vuelve a intentarlo")
L = []
if Destino == Origen:
    print("Origen y destino iguales, acabamos")
else:
    Recorrido.append(Origen)
    while Recorrido[-1] != Destino:
        Lv = city[Recorrido[-1]][1]
        for i in Lv:
            flag = False
            for j in Recorrido:
                if i == j:
                    flag = True
            if flag == False:
                city[i][4] = 2 * (6371000) * asin(sqrt(
                    pow(sin(pi / 360 * (city[Destino][2][0] - city[i][2][0])), 2) + pow(
                        sin(pi / 360 * (city[Destino][2][1] - city[i][2][1])), 2)))
                if L_i == []:
                    L_i.append(i)
                else:
                    while flag == False:
                        if (city[i][4] >= city[L_i[-1]][4]):
                            L_d.append(L_i[-1])
                            L_i.pop(-1)
                            if L_i == []:
                                flag = True
                        else:
                            flag = True
                    L_i.append(i)
                    while L_d != []:
                        L_i.append(L_d[-1])
                        L_d.pop(-1)
        city[Recorrido[-1]][3] = L_i
        Recorrido.append(L_i[-1])
        L_i = []
print("         Recorrido: ")
for i in Recorrido:
    print("              ", city[i][0])


