class Nodo:
    def __init__(self, ciudad, distancia, hijos):
        self.ciudad = ciudad
        self.hijos = hijos
        self.distancia = distancia

    def return_hijos(self):
        print(Nodo.hijos)

    def return_ciudad(self):
        print(Nodo.ciudad)

    def return_distancia(self):
        print(Nodo.distancia)


### Vecinos
A = "Acayucan"
B = "Boca del río"
C = "Coatzacoalcos"
AD = "Agua Dulce"
HJ = "Huatla de Jiménez"
F = "Fortín de las Flores"
H = "Huatusco"
J = "Joachín"
M = "Minatitlan"
N = "El Nigromante"
O = "Otatitlán"
P = "Papantla"
Alv = "Alvarado"
Tec = "Tecolutla"
Tez = "Teziutlán"
Sat = "San Andrés Tuxtla"
V = "Vega de Alatorre"
X = "Xalapa"
Y = "Yanga"
Z = "Zempoala"
####################################################################3


A = Nodo("Acayucan", None, None)
B = Nodo("Boca del río", None, None)
C = Nodo("Coatzacoalcos", None, None)
AD = Nodo("Agua Dulce", None, None)
HJ = Nodo("Huatla de Jiménez", None, None)
F = Nodo("Fortín de las Flores", None, None)
H = Nodo("Huatusco", None, None)
J = Nodo("Joachín", None, None)
M = Nodo("Minatitlan", None, None)
N = Nodo("El Nigromante", None, None)
O = Nodo("Otatitlán", None, None)
P = Nodo("Papantla", None, None)
Alv = Nodo("Alvarado", None, None)
Tec = Nodo("Tecolutla", None, None)
Tez = Nodo("Teziutlán", None, None)
Sat = Nodo("San Andrés Tuxtla", None, None)
V = Nodo("Vega de Alatorre", None, None)
X = Nodo("Xalapa", None, None)
Y = Nodo("Yanga", None, None)
Z = Nodo("Zempoala", None, None)


######################################################################
def Vecinos(x):
    if x == A:
        return [M, Sat, N]
    if x == B:
        return [Alv, J, X, Z]
    if x == C:
        return [AD, M, Sat]
    if x == AD:
        return [C]
    if x == HJ:
        return [O, F]
    if x == F:
        return [HJ, Y, H]
    if x == H:
        return [F, X]
    if x == J:
        return [O, B, Y]
    if x == M:
        return [C, A]
    if x == N:
        return [A, O]
    if x == O:
        return [N, Alv, J, HJ]
    if x == P:
        return [Tec, V, Tez]
    if x == Alv:
        return [Sat, O, B]
    if x == Tec:
        return [P, V]
    if x == Tez:
        return [P, X]
    if x == Sat:
        return [C, A, Alv]
    if x == V:
        return [Tec, P, X, Z]
    if x == X:
        return [Tez, V, Z, B, H]
    if x == Y:
        return [F, J]
    if x == Z:
        return [B, X, V]

######################################################################33
#  Aquí se leerá el origen y destino, para luego ejecutar la función que de los valores de distancia

# Para fines de evaluación del código, asigaremos Valores a las distancias
#  Podemos calcular de una vez todas las distancias o solo ir calculando
#  la de los vecinos para optimizar el código

A.distancia=45
B.distancia=25
C.distancia=48
AD.distancia=50
HJ.distancia=39
F.distancia=30
H.distancia=20
J.distancia=30
M.distancia=47
N.distancia=40
O.distancia=39
P.distancia=35
Alv.distancia=38
Tec.distancia=30
Tez.distancia=18
Sat.distancia=42
V.distancia=21
X.distancia=0
Y.distancia=34
Z.distancia=15


###############################3#########################################
Recorrido = []
Lv=[]
L=[]
L_i = []
L_d=[]


print("hasta aquí vamos")
#variables a declarar

#flag = boleano
flag=False

#x= Destino   # input("nombre de la ciudad destino")
#y= Origen   # input("nombre de la ciudad de origen")

Destino=X
Origen=AD


if Destino== Origen:
    print("Origen y destino iguales, acabamos")

else:


    Recorrido.append(Origen)
    while Recorrido[-1] != Destino:
        Lv=Vecinos(Recorrido[-1])
        for i in Lv:
            flag=False
            for j in Recorrido:
                if i==j:
                    flag=True
            if flag==False:
                #L_i.append(i)

                if L_i==[]:
                    L_i.append(i)
                else:
                    while flag == False:
                        if (i.distancia >= L_i[-1].distancia):
                            L_d.append(L_i[-1])
                            L_i.pop(-1)
                            if L_i == []:
                                flag = True
                        else:
                            flag=True
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
        Recorrido[-1].hijos = L_i
        #print("Recorrido =",Recorrido)
        #print("L_i =", L_i)
        Recorrido.append(L_i[-1])
        L_i=[]



for i in Recorrido:
    print("Recorrido en    ", i.ciudad)
    #print(i.hijos)
    if i.hijos != None:
        for j in i.hijos:
            print("Vecino:   ",j.ciudad)





