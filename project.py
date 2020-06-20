
from math import sin
from math import cos
from math import asin
from math import sqrt
from math import pi

   #X = nombre [0], Vecinos [1], Coordenadas [2], Hijos [3], Distancia [4]
city = dict(
    A=["Acayucan", ['M', 'Sat', 'N'], [17.94919, -94.91459], None, None],
    B=["Boca del río", ['Alv', 'J', 'X', 'Z'], [19.10627, -96.10632], None, None],
    C=["Coatzacoalcos",  ['AD', 'M', 'Sat'], [18.13447, -94.45898], None, None],
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


#######  Esto es solo temporal, en lo que se calculan las distancias

# Se sustituirá con un for x in city...  Calcula distancia de 'ciudad' a 'destino'

#city['A'][4] = 45
#city['B'][4] = 25
#city['C'][4] = 48
#city['AD'][4] = 50
#city['HJ'][4] = 39
#city['F'][4] = 30
#city['H'][4] = 20
#city['J'][4] = 30
#city['M'][4] = 47
#city['N'][4] = 40
#city['O'][4] = 39
#city['P'][4] = 35
#city['Alv'][4] = 38
#city['Tec'][4] = 30
#city['Tez'][4] = 18
#city['Sat'][4] = 42
#city['V'][4] = 21
#city['X'][4] = 0
#city['Y'][4] = 34
#city['Z'][4] = 15




###############################3#########################################
Recorrido = []
Lv = [] #Se sustituye por city[''][1]
L = []
L_i = []
L_d = []

print("hasta aquí vamos")
# variables a declarar

# flag = boleano
flag = False

# x= Destino   # input("nombre de la ciudad destino")
# y= Origen   # input("nombre de la ciudad de origen")

Destino = 'F'
Origen = 'Alv'
#city[Origen][4]= 2*(6356752.31424)*asin(sqrt(pow(sin(pi/360*(city[Destino][2][0]-city[Origen][2][0])),2)+pow(sin(pi/360*(city[Destino][2][1]-city[Origen][2][1])),2)))
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
                # calculamos distancias R= 6,356,752.31424
                # phi1=city[i][2][0] , Lamda=city[i][2][1]   phi2=city[Destino][2][0] , Lamda2=city[Destino][2][1]
                city[i][4] = 2 * (6356752.31424) * asin(sqrt(
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
for i in Recorrido:
    print("Recorrido en    ", city[i][0])
    #if city[i][3] != None:
        #for j in city[i][3]:
            #print("Vecino:   ", city[j][0])
