

city = dict(
    A=["Acayucan", ['M', 'Sat', 'N'], None, None],
    B=["Boca del río", ['Alv', 'J', 'X', 'Z'], None, None],
    C=["Coatzacoalcos",  ['AD', 'M', 'Sat'], None, None],
    AD=["Agua Dulce", ['C'], None, None],
    HJ=["Huatla de Jiménez", ['O', 'F'], None, None],
    F=["Fortín de las Flores", ['HJ', 'Y', 'H'], None, None],
    H=["Huatusco", ['F', 'X'], None, None],
    J=["Joachín", ['O', 'B', 'Y'], None, None],
    M=["Minatitlán", ['C', 'A'], None, None],
    N=["El Nigromante", ['A', 'O'], None, None],
    O=["Otatitlán", ['N', 'Alv', 'J', 'HJ'], None, None],
    P=["Papantla", ['Tec', 'V', 'Tez'], None, None],
    Alv=["Alvarado", ['Sat', 'O', 'B'], None, None],
    Tec=["Tecolutla", ['P', 'V'], None, None],
    Tez=["Teziutlán", ['P', 'X'], None, None],
    Sat=["San Andrés Tuxtla", ['C', 'A', 'Alv'], None, None],
    V=["Vega de Alatorre", ['Tec', 'P', 'X', 'Z'], None, None],
    X=["Xalapa", ['Tez', 'V', 'Z', 'B', 'H'], None, None],
    Y=["Yanga", ['F', 'J'], None, None],
    Z=["Zempoala", ['B', 'X', 'V'], None, None]
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
