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
Recorrido = []
L = []
L_i = []
# flag = boleano


#x= Destino   # input("nombre de la ciudad destino")
#y= Origen   # input("nombre de la ciudad de origen")

# if Destino== Origen:
#    print("Origen y destino iguales, acabamos")
# else:


#    Recorridox.append(x)
#    while Recorrido[-1]=!Y:
#        L=Vecinos(x)
#        for i in L:
#            flag=False
#            for j in Recorrido:
#                if i==j:
#                    flag=True
#            if flag==False:
#                L_i.append(i)
#        #Aquí debo ordenarlos
#        x.hijos=L_i
