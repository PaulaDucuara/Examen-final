import math


class Physics:
    tetha = 47.5
    u = 0.43
    m1 = 20
    m2 = 7.2

    def __init__(self) -> None:
        pass
        

    def calcular_movimiento(self, tetha, u, m1):
        mx1 = (m1 * 9.8 * math.sin(math.radians(tetha))) - (u * math.cos(math.radians(tetha)))
        i = 0
        while i <= 10:
            self.m2 = i
            my2 = self.m2 * 9.8
            mx1 = round(mx1,2)
            my2 = round(my2,2)

            if mx1 > my2:
                print(i,"Sube")
            else:
                print(i,"baja")
            
            print("\t ",mx1, " ", my2)
            i+=0.5

    def calcular_angulo(self, m1, m2, u):
        salida = "-1"
        
        for i in range(0, 90):
            mx1 = (m1 * 9.8 * math.sin(math.radians(i))) - (u * math.cos(math.radians(i)))
            my2 = m2 * 9.8
            if mx1 == my2:
                salida = "Valor encontrado: ", i
                break
        print(salida)




p = Physics()
print("Calculo de movimiento: \n")
p.calcular_movimiento(55,0.15, 6)

print("Calculo de angulo")
p.calcular_angulo(20,10,0.43)
