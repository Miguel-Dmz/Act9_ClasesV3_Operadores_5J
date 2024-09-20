print("**** ACT 9, CLASES V3 ****")
print("MIGUEL DOMINGUEZ MAT: 22308051281173")
# zona de clases

class opereadores1173:
    # zona de funciones
    def suma1173(self,M,D):
        s1173=M+D
        print(f"la suma de {M} + {D} es igual a {s1173}")
    print("\n")
    print("*** SUMA ***")
    
    # RESTA
    def resta1173(self,M,D):
        print("\n")
        print("*** RESTA ***")
        s1173=M-D
        print(f"la resta de {M} - {D} es igual a {s1173}")
        
    # MULTIPLICACION
    def multi1173(self,M,D):
        print("\n")
        print("*** MULTIPLICACION ***")
        s1173=M*D
        print(f"la multiplicacion de {M} x {D} es igual a {s1173}")
    
    # DIVISION
    def division1173(self,M,D):
        print("\n")
        print("*** DIVISION ***")
        s1173=M/D
        print(f"la DIVISION de {M} / {D} es igual a {s1173}")
        
    # DIVISION
    def modulo1173(self,M,D):
        print("\n")
        print("*** MODULO ***")
        s1173=M%D
        print(f"el modulo de {M} % {D} es igual a {s1173}")
        
    # EXPONENTE
    def exponente1173(self,M,D):
        print("\n")
        print("*** EXPONENTE ***")
        s1173=M**D
        print(f"el exponente de {M} ** {D} es igual a {s1173}")
        
    # COCIENTE
    def cociente1173(self,M,D):
        print("\n")
        print("*** COCIENTE ***")
        s1173=M//D
        print(f"el cociente de {M} // {D} es igual a {s1173}")
# zona de creacion del objeto
miguelon=opereadores1173()

# zona de uso de objetos
miguelon.suma1173(4,8)
miguelon.resta1173(14,8)
miguelon.multi1173(16,8)
miguelon.division1173(50,2)
miguelon.modulo1173(51,9)
miguelon.exponente1173(2,5)
miguelon.cociente1173(10,2)