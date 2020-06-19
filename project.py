
#Le meteré las coordenadas en el tercer lugar del diccionario.
city = dict(
    A=["Acayucan", ['M', 'Sat', 'N'], [17.94919, -94.91459], None],
    B=["Boca del río", ['Alv', 'J', 'X', 'Z'], [19.10627, -96.10632], None],
    C=["Coatzacoalcos",  ['AD', 'M', 'Sat'], [18.13447, -94.45898], None],
    AD=["Agua Dulce", ['C'], [18.14259, -94.1436], None],
    HJ=["Huatla de Jiménez", ['O', 'F'], [18.13108, -96.84314], None],
    F=["Fortín de las Flores", ['HJ', 'Y', 'H'], [18.9017, -96.99896], None],
    H=["Huatusco", ['F', 'X'], [19.14823, -96.96654], None],
    J=["Joachín", ['O', 'B', 'Y'], [18.6407, -96.23095], None],
    M=["Minatitlán", ['C', 'A'], [17.99392, -94.5466], None],
    N=["El Nigromante", ['A', 'O'], [17.76323, -95.75574], None],
    O=["Otatitlán", ['N', 'Alv', 'J', 'HJ'], [18.18106, -96.03439], None],
    P=["Papantla", ['Tec', 'V', 'Tez'], [20.45667, -97.31561], None],
    Alv=["Alvarado", ['Sat', 'O', 'B'], [18.76961, -95.75894], None],
    Tec=["Tecolutla", ['P', 'V'], [20.47955, -97.01012], None],
    Tez=["Teziutlán", ['P', 'X'], [19.81601, -97.35705], None],
    Sat=["San Andrés Tuxtla", ['C', 'A', 'Alv'], [18.44412, -95.21302], None],
    V=["Vega de Alatorre", ['Tec', 'P', 'X', 'Z'], [20.03034, -96.65044], None],
    X=["Xalapa", ['Tez', 'V', 'Z', 'B', 'H'], [19.54377, -96.91018], None],
    Y=["Yanga", ['F', 'J'], [18.82928, -96.80027], None],
    Z=["Zempoala", ['B', 'X', 'V'], [19.44688, -96.40507], None]
)


#######  Esto es solo temporal, en lo que se calculan las distancias

# Se sustituirá con un for x in city...  Calcula distancia de 'ciudad' a 'destino'

city['A'][3] = 45
city['B'][3] = 25
city['C'][3] = 48
city['AD'][3] = 50
city['HJ'][3] = 39
city['F'][3] = 30
city['H'][3] = 20
city['J'][3] = 30
city['M'][3] = 47
city['N'][3] = 40
city['O'][3] = 39
city['P'][3] = 35
city['Alv'][3] = 38
city['Tec'][3] = 30
city['Tez'][3] = 18
city['Sat'][3] = 42
city['V'][3] = 21
city['X'][3] = 0
city['Y'][3] = 34
city['Z'][3] = 15



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

Destino = 'X'
Origen = 'AD'

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
                # L_i.append(i)

                if L_i == []:
                    L_i.append(i)
                else:
                    while flag == False:
                        #if (i.distancia >= L_i[-1].distancia):
                        if (city[i][3] >= city[L_i[-1]][3]):
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

        #                while (L_i != []) & (L_d != []):
        #                    if (L==[])or (L[-1].distancia >= L_i[-1].distancia):
        #                        L.append(L_i[-1])
        #                        L_i.pop(-1)
        #                        while L_d != []:
        #                            L.append(L_d[-1])
        #                            L_d.pop(-1)
        #                    else:
        #                        L_d.appdend(L[-1])
        #                        Lv.pop(-1)
        city[Recorrido[-1]][2] = L_i
        # print("Recorrido =",Recorrido)
        # print("L_i =", L_i)
        Recorrido.append(L_i[-1])
        L_i = []

for i in Recorrido:
    print("Recorrido en    ", city[i][0])
    # print(i.hijos)
    if city[i][2] != None:
        for j in city[i][2]:
            print("Vecino:   ", city[j][0])
