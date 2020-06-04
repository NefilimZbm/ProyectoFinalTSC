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
######################################################################33
#  Aquí se leerá el origen y destino, para luego ejecutar la función que de los valores de distancia

# Para fines de evaluación del código, asigaremos Valores a las distancias
#  Podemos calcular de una vez todas las distancias o solo ir calculando
#  la de los vecinos para optimizar el código

A.distancia=1
B.distancia=2
C.distancia=3
AD.distancia=4
HJ.distancia=5
F.distancia=6
H.distancia=7
J.distancia=8
M.distancia=9
N.distancia=10
O.distancia=11
P.distancia=12
Alv.distancia=13
Tec.distancia=14
Tez.distancia=15
Sat.distancia=16
V.distancia=17
X.distancia=18
Y.distancia=19
Z.distancia=20


###############################3#########################################
Recorrido = []
L = []
L_i = []
L_d=[]


print("hasta aquí vamos")
#variables a declarar

#flag = boleano
flag=False

#x= Destino   # input("nombre de la ciudad destino")
#y= Origen   # input("nombre de la ciudad de origen")

Destino=X
Origen=A


if Destino== Origen:
    print("Origen y destino iguales, acabamos")

else:


    Recorrido.append(Origen)
    while Recorrido[-1] != Destino:
        L=Vecinos(Recorrido[-1])
        for i in L:
            flag=False
            for j in Recorrido:
                if i==j:
                    flag=True
            if flag==False:
                L_i.append(i)
                while (L_i != []) & (L_d != []):
                    if (L==[])or (L[-1].distancia >= L_i[-1].distancia):
                        L.append(L_i[-1])
                        L.pop(-1)
                        while L_d != []:
                            L.append(L_d[-1])
                            L_d.pop(-1)
                    else:
                        L_d.appdend(L[-1])
                        L.pop(-1)
        Recorrido.append(L[-1])

for i in Recorrido:
    print(i.ciudad)
